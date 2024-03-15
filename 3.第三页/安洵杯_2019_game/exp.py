# def check2():
# 	v16 = []
# 	for i in range(len(flag)):
# 		v16.append(flag[v15] -48 )
#         #这个位置其实是数字得char和int转化
# 	for i in range(9):
# 		for j in range(9):
# 			if  dog3[9 * i + j] == 0:   # 当D0g3为0的时候v11等于-1244045086
# 				dog3[9 *i + i] = v16[v13]
# 				v13 += 1
#                 #这里形成一个数独游戏得填入
# 	for i in range(9):
# 		for j in range(9):
# 			if dog3[9 * i + j] != sudoku[9 * i + j]:
#                 #注意这里
# 				print("!!!")

# def check1():
# 	v12 = len(flag)>>1
# 	for i in range(len(flag)>>1):
# 		(flag[i],flag[v12+1]) = (flag[v12+1],flag[i])
# 		#前后两部分互换
# 	for i in range(0,len(flag),2):
# 		(flag[i],flag[i+1]) = (flag[i+1],flag[i])
# 		#两位之间互换
# 	for i in range(len(flag)):
# 		flag[i] = ((flag[i]&0xf3)|(~flag[i]&0xc)) - 20

def takereverse(tmp):
    return (tmp & 0xf3)|(~tmp & 0xc)

sudoku =[  1,  4,  5,  3,  2,  7,  6,  9,  8,  8,  3,  9,  6,  5,  4,  1,  2,  7,  6,  7,  2,  8,  1,  9,  5,  4,  3,  4,  9,  6,  1,  8,  5,  3,  7,  2,  2,  1,  8,  4,  7,  3,  9,  5,  6,  7,  5,  3,  2,  9,  6,  4,  8,  1,  3,  6,  7,  5,  4,  2,  8,  1,  9,  9,  8,  4,  7,  6,  1,  2,  3,  5,  5,  2,  1,  9,  3,  8,  7,  6,  4]
D0g3 =[1,  0,  5,  3,  2,  7,  0,  0,  8,  8,  0,  9,  0,  5,  0,  0,  2,  0,  0,  7,  0,  0,  1,  0,  5,  0,  3,  4,  9,  0,  1,  0,  0,  3,  0,  0,  0,  1,  0,  0,  7,  0,  9,  0,  6,  7,  0,  3,  2,  9,  0,  4,  8,  0,  0,  6,  0,  5,  4,  0,  8,  0,  9,  0,  0,  4,  0,  0,  1,  0,  3,  0,  0,  2,  1,  0,  3,  0,  7,  0,  4]
arr = []
for i in range(len(D0g3)):
    if(D0g3[i]== 0 ):
        arr.append(chr(takereverse(sudoku[i]+48+20)))
for i in range(0,40,2):
	(arr[i], arr[i+1]) = (arr[i+1], arr[i])
for i in range(20):
	(arr[i],arr[i+20]) = (arr[i+20], arr[i])

for i in range(40):
	print(arr[i],end="")
