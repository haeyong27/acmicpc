s = '''0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 1 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 0 1 1 1 1 0 0 0 0
0 1 1 1 1 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1
0 0 0 0 0 1 1 1 1 1'''

mapp = []
for i in s.split('\n'):
    mapp.append(list(map(int, i.split(' '))))

for i in mapp:
    print(i)

color = []
for i in range(10):
    for j in range(10):
        if mapp[i][j] == 1:
            color.append((i, j))

temp_map = []
for i in mapp:
    temp_map.append(i[:])


def fill(loc, size):
    x, y = loc
    flag = 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            if 0<=i<10 and 0<=y<10:
                if temp_map[i][j] == 0:
                    return False
            else:
                return False

    if flag == 0:
        for i in range(x, x+size):
            for j in range(y, y+size):
                temp_map[i][j] = 1
    return True


def check_complete():
    for i in range(10):
        if 1 in temp_map[i]:
            return False
    return True


def find_loc():
    for i in range(10):
        for j in range(10):
            if temp_map[i][j] == 1:
                return (i, j)


def dfs(cnt):

    x, y = find_loc()
    for i in reversed(range(1, 6)):
        if fill([x, y], i):
            break
    if check_complete():
        break
    dfs(cnt+1)




    
