data = list(open(r'D:\CTF_Study\Reverse\BUU\4.第四页\[NPUCTF2020]EzObfus-Chapter2\re.exe', 'rb').read())
for i in range(22):
    data[0x15a06] = i 
    filename = f"aaa{i}.exe"
    open(filename, 'wb').write(bytes(data))