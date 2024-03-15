with open(r'D:\CTF_Study\Reverse\BUU\5.第五页\[FlareOn2]gdssagh\gdssagh.exe', "rb") as f:
    b = f.read()[0x413:0xCC1A5]
    import base64
    b = base64.b64decode(b)
    ff = open(r"D:\CTF_Study\Reverse\BUU\5.第五页\[FlareOn2]gdssagh\out", "wb")
    ff.write(b)
    ff.close()