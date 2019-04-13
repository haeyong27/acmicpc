n, m = map(int, input().split(' '))
ori_map = []
for i in range(n):
    ori_map.append(list(map(int, input().split(' '))))

cctv = []
cctv5 = []
mapp = []
for i in range(n):
    for j in range(m):
        if 1<=ori_map[i][j]<=4:
            cctv.append((i, j))
        if ori_map[i][j] == 5:
            cctv5.append((i, j))

def gamsi5(x, y):
    global ori_map
    tempx = x
    tempy = y
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    for d in range(4):
        x = tempx
        y = tempy
        while(True):
            x = x + dx[d]
            y = y + dy[d]
            if 0<=x<n and 0<=y<m:
                if ori_map[x][y] == 6:
                    break
                if ori_map[x][y] == 0:
                    ori_map[x][y] = '#'
            else:
                break

for x, y in cctv5:
    gamsi5(x, y)

def gamsi(x, y, d):
    global mapp
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    while(True):
        x = x + dx[d]
        y = y + dy[d]
        if 0<=x<n and 0<=y<m:
            if mapp[x][y] == 6:
                break
            if mapp[x][y] == 0:
                mapp[x][y] = '#'
        else:
            break




def tot_gamsi(x, y, d):
    
    if mapp[x][y] == 1:
        gamsi(x, y, d)

    if mapp[x][y] == 2:
        gamsi(x, y, d)
        gamsi(x, y, (d+2)%4)

    if mapp[x][y] == 3:
        gamsi(x, y, d)
        gamsi(x, y, (d+1)%4)

    if mapp[x][y] == 4:
        gamsi(x, y, d)
        gamsi(x, y, (d+1)%4)
        gamsi(x, y, (d+2)%4)

num_cctv = len(cctv)
check = [0 for _ in range(num_cctv)]
temp = []
ans = 9999999

def dfs(cnt):
    global mapp
    global ori_map
    global ans
    if cnt == num_cctv:
        mapp = []
        for i in ori_map:
            mapp.append(i[:])

        for i in range(num_cctv):
            x, y = cctv[i]
            d = temp[i]
            tot_gamsi(x, y, d)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if mapp[i][j] == 0:
                    cnt += 1
        ans = min(ans, cnt)
        return

    for i in range(4):
        if check[cnt] == 1:
            continue
        check[cnt] = 1
        temp.append(i)
        dfs(cnt+1)
        temp.pop()
        check[cnt] = 0

dfs(0)
print(ans)
