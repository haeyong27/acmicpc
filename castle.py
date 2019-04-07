import itertools

n, m, d = map(int, input().split(' '))
comb = itertools.combinations([i for i in range(m)], 3)

mapp = []
for i in range(n):
    mapp.append(list(map(int,input().split(' '))))

temp_map = []
for i in mapp:
    temp_map.append(i[:])

def move():
    global temp_map
    for i in reversed(range(1, n)):
        temp_map[i] = list(temp_map[i-1])
    temp_map[0] = [0 for _ in range(m)]

dx = [0, -1, 0]
dy = [-1, 0, 1]

def kill(loc):
    global temp_map
    stack = []
    x, y = n-1, loc
    if temp_map[x][y] == 1:
        return (x, y)
    stack.append((x, y))
    check = [[0 for _ in range(m)] for _ in range(n)]
    dist = [[1 for _ in range(m)] for _ in range(n)]
    while(stack):
        x, y = stack.pop(0)
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and check[nx][ny] == 0 and dist[x][y] < d:
                if temp_map[nx][ny] == 1:
                    return (nx, ny)
                check[nx][ny] = 1
                dist[nx][ny] = dist[x][y]+1
                stack.append((nx, ny))
    return (-1, -1)


def killmove(archers):
    global temp_map
    #kill list 만들기
    kill_list = [] 
    for archer in archers:
        x, y = kill(archer)
        if x == -1:
            continue
        if (x, y) not in kill_list:
            kill_list.append((x, y))
    for x, y in kill_list:
        temp_map[x][y] = 0
    move()

    return len(kill_list)



def solution():
    global temp_map
    ans = 0
    for c in comb:
        cnt = 0
        temp_map = []

        for j in mapp:
            temp_map.append(j[:])

        for _ in range(n):
            cnt += killmove(c)

        ans = max(ans, cnt)
    print(ans)


solution()
