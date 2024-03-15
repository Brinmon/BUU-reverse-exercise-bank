def explore_maze(maze,x,y):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]  # 记录访问状态
    path = []  # 记录路径

    def dfs(row, col):
        # 检查边界和是否已访问
        if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col]:
            return False

        # 检查是否达到终点
        if maze[row][col] == 101:
            path.append((row, col))
            return True

        # 检查当前位置是否可通行
        if maze[row][col] == 1:
            return False

        visited[row][col] = True
        path.append((row, col))

        # 递归探索四个方向
        if dfs(row, col + 1) or dfs(row + 1, col) or dfs(row, col - 1) or dfs(row - 1, col):
            return True

        # 如果四个方向都无法到达终点，则回溯
        path.pop()
        return False

    dfs(y, x)
    return path

def get_move_direction(start, target):
    start_row, start_col = start
    target_row, target_col = target

    if target_col > start_col:
        return "d"  # 向右移动
    elif target_col < start_col:
        return "a"  # 向左移动
    elif target_row < start_row:
        return "w"  # 向上移动
    elif target_row > start_row:
        return "s"  # 向下移动
    else:
        return ""  # 没有移动

maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [1,0,1,1,1,1,0,0,0,101,0,0,0,1,1,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1],
    [1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

start_X = 5
start_y = 10
path = explore_maze(maze,start_X,start_y)
temp = (0,0)
plaintext = ""
if path:
    print("Path found:")
    for row, col in path:
        current = (row, col)
        if(current == (10,5)):
            continue
        ch = get_move_direction(temp,current)
        plaintext +=ch
        print(ch,end="")
        temp = (row, col)
else:
    print("No path found.")
from Crypto.Cipher import Blowfish
from Crypto.Util.number import bytes_to_long
key=b"\x00\x0F\x1A\x01\x35\x3A\x3B\x20"
blowfish=Blowfish.new(key,Blowfish.MODE_ECB)
text = plaintext.encode('utf-8')
print(hex(bytes_to_long(blowfish.encrypt(text[:8]))).replace('0x','').replace('L','')+hex(bytes_to_long(blowfish.encrypt(text[8:]))).replace('0x','').replace('L',''))
#db824ef8605c5235b4bbacfa2ff8e087
