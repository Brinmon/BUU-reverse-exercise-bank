import angr
import binascii
from capstone import *

p = angr.Project(r'D:\CTF_Study\Reverse\BUU\4.第四页\[FlareOn4]greek_to_me\greek_to_me.exe', load_options={'auto_load_libs': False})

for buf in range(0xa2,0xa3): #已知key是0xa2，为了减少时间就直接使用0xa2到0xa3
    print("Using {0}".format(buf))
    # Variable to store the bits written to disk using IDA 将从ida获取下来的数据存入asm变量中
    asm = None
    # Store the output from the first de-obfuscation routine  将解密出来的代码存储在变量b2中
    b2 = []
    # Read in bytes written to file from IDA 读取从ida上dump出来的数据
    with open(r'D:\CTF_Study\Reverse\BUU\4.第四页\[FlareOn4]greek_to_me\greek_to_me_buffer.asm', 'rb') as f:
        asm = f.read()

    print(asm)
    
    # Re-implement loc_401039  开始逆运算数据
    dl = buf
    for byte in asm:
        bl = byte
        bl = bl ^ dl
        bl = bl & 0xff #由于汇编时只用了寄存器的低八位要及时清理溢出
        bl = bl + 0x22
        bl = bl & 0xff #由于汇编时只用了寄存器的低八位要及时清理溢出
        b2.append(bl)

    # Set up angr to "run" sub_4011E6，sub_4011E6()这个函数有两个参数
    s = p.factory.blank_state(addr=0x4011E6)
    s.mem[s.regs.esp+4:].dword = 0x1000    # Angr memory location to hold the xor'ed and add'ed bytes 在栈上放置一个地址0x1000，用来存放解密后的汇编代码，其实也是这个函数的参数
    s.mem[s.regs.esp+8:].dword = 0x79 # Length of ASM   这个函数的另一个参数
    
    asm = bytes(b2) #start: b'\xb3e\x88]\xd5\xc6E\xd6t\xb2_\x88U\xd7\xc6E\xd8t\xc6E\xd9u\x88U\xda\xc6E\xdbb\xc6E\xdcr\xc6E\xddu\xc6E\xdet\x88]\xdf\x88U\xe0\xc6E\xe1f\xc6E\xe2o\xc6E\xe3r\xc6E\xe4c\x88]\xe5\xc6E\xe6@\xc6E\xe7f\xc6E\xe8l\xc6E\xe9a\xc6E\xear\x88]\xeb\xc6E\xec-\xc6E\xedo\xc6E\xeen\xc6E\xef.\xc6E\xf0c\xc6E\xf1o\xc6E\xf2m\xc6E\xf3\x00'
    hex_str = binascii.hexlify(asm).decode('utf-8')
    print("hex_str",hex_str)
    hex_int = int(hex_str, 16)
    s.memory.store(0x1000, s.se.BVV(hex_int, 0x79 * 8)) #向0x1000这个地址位置写入解密完成的汇编代码
    print("end:",hex_int)
    # Create a simulation manager... 创建符号执行！
    simgr = p.factory.simulation_manager(s)
    
    # Tell Angr where to go, though there is only one way through this function,
    # we just need to stop after ax is set
    simgr.explore(find=0x401268) #运行到sub_4011E6()这个函数解密完成

    # Once ax is set, check to see if the value in ax matches the comparison value 设置ax后，检查ax中的值是否与比较值匹配
    for found in simgr.found:
        print(hex(found.solver.eval(found.regs.ax)))
        # Comparison check
        if hex(found.solver.eval(found.regs.ax)) == '0xfb5e':   #encode(&loc_40107C, 0x79u) == 0xFB5E 这个函数有返回值，用于检测key是否正确
            # 成功匹配！！！
            print("解密的key是：",buf)
            print("解密结果：",asm)
            bl = ''
            dl = ''
            flag = []
            md = Cs(CS_ARCH_X86, CS_MODE_32) #使用capstone库进行反汇编，将解密的汇编代码反汇编成汇编代码
            for i in md.disasm(asm, 0x1000):
                flag_char = ''
                # The if statements do the work of interpreting the ASCII codes to their value counterpart ，运用字符匹配提取出汇编代码中的字符串
                if i.op_str.split(',')[1].strip() == 'dl':
                    flag_char = dl
                elif i.op_str.split(',')[1].strip() == 'bl':
                    flag_char = bl
                elif i.op_str.split(',')[0].startswith("byte ptr"):
                    flag_char = chr(int(i.op_str.split(',')[1].strip(), 16))
                elif i.op_str.split(',')[0].startswith('bl'):
                    bl = chr(int(i.op_str.split(',')[1].strip(), 16))
                elif i.op_str.split(',')[0].startswith('dl'):
                    dl = chr(int(i.op_str.split(',')[1].strip(), 16))

                if (flag_char):
                    flag.append(flag_char.strip())

                print("0x%x\t%s\t%s\t%s" %(i.address, i.mnemonic, i.op_str, flag_char))

            print("flag:",''.join(flag))
            pass
