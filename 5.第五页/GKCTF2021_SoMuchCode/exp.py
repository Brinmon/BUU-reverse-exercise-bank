import time
from LyScript64 import MyDebug
from LyScriptTools64 import DebugControl


if __name__ == "__main__":
    dbg = MyDebug()
    connect_flag = dbg.connect()
    print("连接状态: {}".format(connect_flag))

    debug = DebugControl(dbg)

    ref = debug.script_initdebug(r"d:/CTF_Study/Reverse/BUU/5.第五页/GKCTF2021_SoMuchCode/SoMuchCode副本.exe")
    print("程序挂载状态: {}".format(ref))
    
    debug.script_rundebug() #运行程序
    time.sleep(0.1)
    ref = dbg.set_breakpoint(0x0007FF711905B20) #下断点
    debug.script_rundebug()
    print("下断点结果: {}".format(ref))

    r14dlist = []
    idx = 0
    while idx<32:
        if(dbg.check_breakpoint(0x0007FF711905B20)):
            r14d = dbg.get_register("r14d")
            r14dlist.append(r14d)
            debug.script_rundebug()
            time.sleep(0.01) #需要等待不然会检测到多次使用断点
            idx +=1
    print(r14dlist)