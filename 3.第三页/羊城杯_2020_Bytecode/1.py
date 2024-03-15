"""bytecode_file = open(r'D:\CTF_Study\Reverse\BUU\The 3 Page\羊城杯_2020_Bytecode\attachment.txt', 'r')
bytecode = bytecode_file.read()
bytecode_file.close()

exec(bytecode)"""

import dis

def disassemble_pyc(pyc_file_path):
    with open(pyc_file_path, 'rb') as pyc_file:
        magic = pyc_file.read(4)  # 读取文件头部的魔数
        pyc_file.read(4)  # 跳过编译时间戳
        code_object = dis._get_code_object(pyc_file)  # 获取字节码对应的 code object
        dis.dis(code_object)  # 反汇编字节码

# 指定.pyc文件路径
pyc_file_path = r'D:\CTF_Study\Reverse\Geek Challenge 2023\小黄鸭\小黄鸭\小黄鸭.exe_extracted\struct.pyc'

# 调用函数进行反汇编
disassemble_pyc(pyc_file_path)