import numpy as np
from PIL import Image
import scipy.misc

with open (r"D:\CTF_Study\Reverse\BUU\5.第五页\[UTCTF2020]png2\attachment.png2", "rb") as f:
    data = f.read()

image = np.zeros( (1487, 648, 3), dtype = np.uint8 )

x=0
y=0

for i in range (21, len(data), 3):
    red = data[i]
    blue = data[i+1]
    green = data[i+1]

    image[x,y] = [red, blue, green]

    x += 1
    if x>=1487:
        x=0
        y+=1

Image.fromarray(image).convert('L').save(r"D:\CTF_Study\Reverse\BUU\5.第五页\[UTCTF2020]png2\solve.png")