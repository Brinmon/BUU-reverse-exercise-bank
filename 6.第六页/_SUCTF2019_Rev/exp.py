a = [0xD8, 0xDE, 0xC8, 0xDF, 0xCD]
for i in range(len(a)):
    print(chr(a[i]^0xab),end="")
print("\n")

from z3 import *

x = BitVec('x',32)
s = Solver()

s.add(x&1==0)
s.add((1234 * x + 5678) / 4396 ^ 0xABCDDCBA == 0xABCDB8B9)
s.add((2334 * x + 9875) / 7777 ^ 0x12336790 == 0x1233FC70)

if s.check() == sat :
    print(s.model())

# [x = 31415926]