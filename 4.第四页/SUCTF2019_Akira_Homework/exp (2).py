import time
from LyScript64 import MyDebug
from LyScriptTools64 import DebugControl


if __name__ == "__main__":
    dbg = MyDebug()
    connect_flag = dbg.connect()
    print("连接状态: {}".format(connect_flag))

    debug = DebugControl(dbg)

    ref = debug.script_initdebug(r"d:/CTF_Study/Reverse/BUU/4.第四页/SUCTF2019_Akira_Homework/WinRevCopy.exe")
    print("程序挂载状态: {}".format(ref))
    debug.script_rundebug() #运行程序
    time.sleep(0.1)
    ref = dbg.set_breakpoint(0x140009B52) #下断点
    print("下断点结果: {}".format(ref))
    # debug.script_rundebug() #运行程序
    
    print("开始")
    pDllBuff = []
    while True:
        if(dbg.check_breakpoint(0x140009B52)):
            for i in range(19456):
                ref = dbg.read_memory_byte(0x1400111A0+i)
                pDllBuff.append(ref)
            
            dll_data = bytearray(pDllBuff)  # 将DLL数据转换为字节数组
            # print(dll_data)
            with open("Test.DLL", "wb+") as file:
                file.write(dll_data)
            print("成功dump！")
            dbg.close()
            break