n, m = map(int, input().split(' '))

mapp = []
for i in range(n):
    mapp.append(list(input()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def melt():
    global mapp
    global dx, dy
    
    melt_list = []
    check = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if mapp[i][j] != 'X':
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0<=ni<n and 0<=nj<m and mapp[ni][nj] == 'X' and check[ni][nj] == 0:
                        melt_list.append((ni, nj))
                        check[ni][nj] = 1
    
    
    for x, y in melt_list:
        mapp[x][y] = '.'

#백조위치 찾기
swan = []
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 'L':
            swan.append((i, j))

def find():
    global mapp
    global dx, dy
    stack = [swan[0]]
    check = [[0 for _ in range(m)] for _ in range(n)]

    while(stack):
        x, y = stack.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and check[nx][ny] == 0 and mapp[nx][ny] != 'X':
                if (nx, ny) == swan[1]:
                    return True
                check[nx][ny] = 1
                stack.append((nx, ny))
    return False
flag = 0

def dfs(x, y):
    global mapp
    global dx, dy
    global swan
    global ans
    global check
    global flag
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and check[nx][ny] == 0 and mapp[nx][ny] != 'X':
            if mapp[nx][ny] == 'L':
                print(ans)
                exit()
            check[nx][ny] = 1
            dfs(nx, ny)


ans = 0
while(True):
    check = [[0 for _ in range(m)] for _ in range(n)]
    check[swan[0][0]][swan[0][1]] =1 
    dfs(swan[0][0], swan[0][1])
    melt()
    ans += 1
