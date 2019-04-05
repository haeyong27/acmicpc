import copy
from itertools import combinations

n, m = map(int, input().split(' '))
ans = 0
mapp = []
for i in range(n):
    mapp.append(list(map(int, input().split(' '))))

wall = []
virus = []
load = []

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1:
            wall.append((i, j))
        if mapp[i][j] == 2:
            virus.append((i, j))
        if mapp[i][j] == 0:
            load.append((i, j))


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def spread(temp_map):
    check = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    temp_virus = virus[:]
    while(temp_virus):
        x, y = temp_virus.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and temp_map[nx][ny] == 0 and check[nx][ny] == 0:
                check[nx][ny] = 1
                temp_virus.append((nx,ny))
                temp_map[nx][ny] = 2

    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                cnt += 1
    return cnt


check_load = [0 for _ in range(len(load))]
temp_wall = []

comb = combinations(load, 3)
for i in comb:
#     temp_map = copy.deepcopy(mapp)
    temp_map = [] # 딥카피보다 빠름
    for i in mapp:
        temp_map.append(i[:])


    for x, y in i:
        temp_map[x][y] = 1
    ans = max(ans, spread(temp_map))

print(ans)


# def dfs(idx, cnt):
#     global ans

#     if cnt == 3:
#         temp_map = copy.deepcopy(mapp)
#         for x, y in temp_wall:
#             temp_map[x][y] = 1
#         ans = max(ans, spread(temp_map))
#         return

#     for i in range(idx, len(load)):
#         if check_load[i] == 1:
#             continue
#         temp_wall.append(load[i])
#         check_load[i] = 1
#         dfs(i, cnt + 1)
#         temp_wall.pop()
#         check_load[i] = 0

# dfs(0,0)
# print(ans)
