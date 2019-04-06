#맵을 한칸씩 위로 올라가면서, move만들필요 없이 
n, m, d = map(int, input().split(' '))
mapp = []
for i in range(n):
    mapp.append(list(map(int,input().split(' '))))

temp_map = []
for i in mapp:
    temp_map.append(i[:])

def move():

    for i in reversed(range(1, n)):
        temp_map[i] = list(temp_map[i-1])
    temp_map[0] = [0 for _ in range(m)]

dx = [0, -1, 0]
dy = [-1, 0, 1]


def kill(archer):
    cnt = 0
    kill_list = []

    def archer_kill(loc):
        check = [[0 for _ in range(m)] for _ in range(n)]
        dist = [[0 for _ in range(m)] for _ in range(n)]
        archer_stack = [(n-1, loc)]
        while(archer_stack):
            x, y = archer_stack.pop(0)
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m and check[nx][ny] == 0 and dist[nx][ny] < d:
                    if temp_map[nx][ny] == 1:
                        if (nx, ny) not in kill_list:
                            kill_list.append((nx, ny))
                        return
                    check[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    archer_stack.append((nx, ny))

    for i in archer:
        archer_kill(i)

    for x, y in kill_list:
        temp_map[x][y] = 0
        cnt += 1

    return cnt

dfs_check = [0 for _ in range(m)]
dfs_temp_list = []

ans = 0

comb_list = []

def dfs(idx, cnt):
    global ans
    if cnt == 3:
        comb_list.append(dfs_temp_list)
        return
    
    for i in range(idx, m):
        if dfs_check[i] == 1:
            continue
        dfs_check[i] = 1
        dfs_temp_list.append(i)
        dfs(i, cnt+1)
        dfs_temp_list.pop()
        dfs_check[i] = 0

dfs(0, 0)
print(comb_list)

temp_map = []
for i in mapp:
    temp_map.append(i[:])

a = 0
for i in range(n):
    a += kill(dfs_temp_list)
    move()
ans = max(ans, a)
