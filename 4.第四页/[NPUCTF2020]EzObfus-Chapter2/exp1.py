import subprocess
flag = ''
for i in range(22):
    for j in range(0x21, 0x7f):
        filename = f".\\aaa{i}.exe"
        p = subprocess.Popen(filename, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print('pid', p.pid)
        tmp = ((flag+chr(j)).ljust(22,'A')+'\n').encode()
        print('tmp:', tmp)
        p.stdin.write(tmp)
        p.stdin.close()
        out = p.stdout.read()
        p.stdout.close()
        print("A:",out)
        if b'Error' not in out:
            flag += chr(j)
            print(flag)
            break
#npuctf{WDNMD_LJ_OBFU!}