import binascii
import struct
from unicorn import *
from unicorn.x86_const import *
from capstone import *
CHECKSUM_CODE = binascii.unhexlify(
    '55 8B EC 51 8B 55 0C B9 FF 00 00 00 89 4D FC 85 D2 74 51 53 8B 5D 08 56 57 '
    '6A 14 58 66 8B 7D FC 3B D0 8B F2 0F 47 F0 2B D6 0F B6 03 66 03 F8 66 89 7D '
    'FC 03 4D FC 43 83 EE 01 75 ED 0F B6 45 FC 66 C1 EF 08 66 03 C7 0F B7 C0 89 '
    '45 FC 0F B6 C1 66 C1 E9 08 66 03 C1 0F B7 C8 6A 14 58 85 D2 75 BB 5F 5E 5B '
    '0F B6 55 FC 8B C1 C1 E1 08 25 00 FF 00 00 03 C1 66 8B 4D FC 66 C1 E9 08 66 '
    '03 D1 66 0B C2'.replace(' ', ''))
ENCODED_BYTES = binascii.unhexlify(
    '33 E1 C4 99 11 06 81 16 F0 32 9F C4 91 17 06 81 14 F0 06 81 15 F1 C4 91 1A '
    '06 81 1B E2 06 81 18 F2 06 81 19 F1 06 81 1E F0 C4 99 1F C4 91 1C 06 81 1D '
    'E6 06 81 62 EF 06 81 63 F2 06 81 60 E3 C4 99 61 06 81 66 BC 06 81 67 E6 06 '
    '81 64 E8 06 81 65 9D 06 81 6A F2 C4 99 6B 06 81 68 A9 06 81 69 EF 06 81 6E '
    'EE 06 81 6F AE 06 81 6C E3 06 81 6D EF 06 81 72 E9 06 81 73 7C'.replace(' ',
    ''))

def decode_bytes(i):
    decoded_bytes = ""
    for byte in ENCODED_BYTES:
        decoded_bytes += chr((((byte ^ i) & 0xFF) + 0x22) & 0xFF)
    return decoded_bytes
 
def emulate_checksum(decoded_bytes):
    # establish memory addresses for checksum code, stack, and decoded bytes
    address = 0x400000
    stack_addr = 0x410000
    dec_bytes_addr = 0x420000
    # write checksum code and decoded bytes into memory
    mu = Uc(UC_ARCH_X86, UC_MODE_32)
    mu.mem_map(address, 2 * 1024 * 1024)
    mu.mem_write(address, CHECKSUM_CODE)
    mu.mem_write(dec_bytes_addr, bytes(decoded_bytes,'latin-1'))
    # place the address of decoded bytes and size on the stack
    mu.reg_write(UC_X86_REG_ESP, stack_addr)
    mu.mem_write(stack_addr + 4, struct.pack('<I', dec_bytes_addr))
    mu.mem_write(stack_addr + 8, struct.pack('<I', 0x79))
    # emulate and read result in AX
    mu.emu_start(address, address + len(CHECKSUM_CODE))
    checksum = mu.reg_read(UC_X86_REG_AX)
    return checksum


if __name__ == "__main__":
    flag=[]

    for i in range(0xa1, 0xa3):
        decoded_bytes = decode_bytes(i)
        checksum = emulate_checksum(decoded_bytes)
        if checksum == 0xFB5E:
            print('Checksum matched with byte %X' % i)
            print('Decoded bytes disassembly:')
            md = Cs(CS_ARCH_X86, CS_MODE_32)
            for i in md.disasm(bytes(decoded_bytes,'latin-1'), 0x40107C):
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