n, m = map(int, input().split())
mapp = []
for i in range(n):
    mapp.append(list(input()))

water_stack = []
gosum = []
dongul = []
for i in range(n):
    for j in range(m):
        if mapp[i][j] == '*':
            water_stack.append((i, j))
        elif mapp[i][j] == 'D':
            dongul.append((i, j))
        elif mapp[i][j] == 'S':
            gosum.append((i, j))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
while (gosum):
    #물 번지기
    water_stack_temp = water_stack[:]
    water_stack = []

    while (water_stack_temp):
        wx, wy = water_stack_temp.pop(0)
        for i in range(4):
            nx = wx + dx[i]
            ny = wy + dy[i]
            if 0<=nx<n and 0<=ny<m and mapp[nx][ny] == '.':
                mapp[nx][ny] = '*'
                water_stack.append((nx, ny))
        
    ans += 1
    gosum_temp = gosum[:]
    gosum = []
    while gosum_temp:
        x, y = gosum_temp.pop(0)
        for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) == dongul[0]:
                    print(ans)
                    exit()
                if 0<=nx<n and 0<=ny<m and mapp[nx][ny] == '.':
                    mapp[nx][ny] = 'S'
                    gosum.append((nx, ny))
    
print('KAKTUS')
