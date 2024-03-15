def reverse(x):
    result = 0
    for i in range(8):
        if (x >> i) & 1:
            result |= 1 << (8 - 1 - i)
    return result

data = open('out.png', 'rb').read()
output = b''

for i in data:
    output += bytes(reverse(i))

print(output[0:4])

with open('correct.exe', 'wb') as file:
    file.write(output)
