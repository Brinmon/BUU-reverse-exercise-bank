import base64
def read_file(file_path):
    lines = []
    
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    
    return lines

def process_strings(strings):
    processed_strings = []
    
    for string in strings:
        if string.endswith("=="):
            processed_string = ""
            remove_next_char = False
            
            for char in string:
                if char == "Q" and  remove_next_char == False:
                    remove_next_char = True
                    continue
                if char == "1" and  remove_next_char == False:
                    remove_next_char = True
                    continue
                if remove_next_char:
                    processed_string += char
            remove_next_char = False
            processed_strings.append(processed_string)
    
    return processed_strings

def base64_stego(lines):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    flag = ''
    temp = 0
    digit = 0
    for i in lines:
        if i[-1] != '=':
            continue
        elif i[-2] != '=':
            digit += 2
            temp = (temp << 2) + (alphabet.find(i[-2]) & 0x3)
        else:
            digit += 4
            temp = (temp << 4) + (alphabet.find(i[-3]) & 0xf)
        if digit == 8:
            digit = 0
            flag += chr(temp)
            temp = 0
        elif digit > 8:
            digit = 2
            flag += chr(temp >> 2)
            temp = temp & 0x3
    return flag

poestring ="""眼前重复的风景,
渐渐模糊了约定,
星空下流浪的你,
仍然秘密的距离,
温度消失的瞬间,
无法触摸的明天,
没有引力的世界,
没有脚印的光年,
还在等着你出现,
日日夜夜自转的行星,
到处遮满别人的背影,
让风吹散混乱的呼吸,
快快清醒~
静静照亮原来的自己,
天空洒满忽然的光明,
眼中只要绚烂的天际,
再飞行!
我勇敢地抬起头,
看着茫茫的宇宙,
多少未知的星球,
有没有通向未来路口,
亲爱的伙伴,
让我们一起点燃,
勇气和信念,
在遥远的天边,
银河边缘,
有一片神奇的彩虹海,
和我一起冒险,
飞向另一个世界,
在遥远的天边,
银河边缘,
有一片神奇的彩虹海,
和我一起冒险,
飞向另一个世界,
super magic world~~"""
poestring_list = poestring.split('\n')
print("poestring_list长度：",len(poestring_list))
my_list = [''] * 35

strings = read_file(r'D:\CTF_Study\Reverse\BUU\4.第四页\[NPUCTF2020]芜湖\2.txt')
processed = process_strings(strings)
print("processed长度：",len(processed))
for i in range(len(processed)):
    print(base64.b64decode(processed[i]).decode())
    for j in range(len(poestring_list)):
        if base64.b64decode(processed[i]).decode() == poestring_list[j]:
            if my_list[j] == '':
                my_list[j] = processed[i]
print(my_list)



a = ["55y85YmN6YeN5aSN55qE6aOO5pmvLG==",
"5riQ5riQ5qih57OK5LqG57qm5a6aLO==",
"5pif56m65LiL5rWB5rWq55qE5L2gLH==",
"5LuN54S256eY5a+G55qE6Led56a7LA==",
"5rip5bqm5raI5aSx55qE556s6Ze0LH==",
"5peg5rOV6Kem5pG455qE5piO5aSpLF==",
"5rKh5pyJ5byV5Yqb55qE5LiW55WMLG==",
"5rKh5pyJ6ISa5Y2w55qE5YWJ5bm0LD==",
"6L+Y5Zyo562J552A5L2g5Ye6546wLH==",
"5pel5pel5aSc5aSc6Ieq6L2s55qE6KGM5pifLE==",
"5Yiw5aSE6YGu5ruh5Yir5Lq655qE6IOM5b2xLG==",
"6K6p6aOO5ZC55pWj5re35Lmx55qE5ZG85ZC4LG==",
"5b+r5b+r5riF6YaSfn==",
"6Z2Z6Z2Z54Wn5Lqu5Y6f5p2l55qE6Ieq5bexLL==",
"5aSp56m65rSS5ruh5b+954S255qE5YWJ5piOLE==",
"55y85Lit5Y+q6KaB57ua54OC55qE5aSp6ZmFLG==",
"5YaN6aOe6KGMIW==",
"5oiR5YuH5pWi5Zyw5oqs6LW35aS0LM==",
"55yL552A6Iyr6Iyr55qE5a6H5a6ZLH==",
"5aSa5bCR5pyq55+l55qE5pif55CDLJ==",
"5pyJ5rKh5pyJ6YCa5ZCR5pyq5p2l6Lev5Y+jLD==",
"5Lqy54ix55qE5LyZ5Ly0LB==",
"6K6p5oiR5Lus5LiA6LW354K554eDLG==",
"5YuH5rCU5ZKM5L+h5b+1LO==",
"5Zyo6YGl6L+c55qE5aSp6L65LG==",
"6ZO25rKz6L6557yYLH==",
"5pyJ5LiA54mH56We5aWH55qE5b2p6Jm55rW3LC==",
"5ZKM5oiR5LiA6LW35YaS6ZmpLB==",
"6aOe5ZCR5Y+m5LiA5Liq5LiW55WMLC==",
"5Zyo6YGl6L+c55qE5aSp6L65LB==",
"6ZO25rKz6L6557yYLC==",
"5pyJ5LiA54mH56We5aWH55qE5b2p6Jm55rW3LB==",
"5ZKM5oiR5LiA6LW35YaS6ZmpLH==",
"6aOe5ZCR5Y+m5LiA5Liq5LiW55WMLN==",
"c3VwZXIgbWFnaWMgd29ybGR+fg=="]

for i in range(len(my_list)):
    if(my_list[i] != a[i]):
        print(my_list[i])
        print(a[i])
print(base64_stego(my_list))
#npuctf{Fly1ng!!!}