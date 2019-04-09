n = int(input())
mapp = []
for i in range(n):
    mapp.append(list(map(int, input().split(' '))))
cnt = 0

def dfs(loc, dir):
    global cnt
    x, y = loc
    if (x, y) == (n-1, n-1):
        cnt += 1
    
    if dir == 1 :
        #오른쪽으로
        y += 1
        if y < n:
            if mapp[x][y] == 0:
                dfs([x, y], 1)
        y -= 1
        # 오른쪽아래로        
        x += 1
        y += 1
        if x<n and y<n:
            if mapp[x][y] == 0 and mapp[x-1][y] == 0 and mapp[x][y-1] == 0:
                dfs([x, y], 2)
        x -= 1
        y -= 1

    if dir == 2 :
        #오른쪽으로
        y += 1
        if y < n:
            if mapp[x][y] == 0:
                dfs([x, y], 1)
        y -= 1
        # 오른쪽아래로        
        x += 1
        y += 1
        if x<n and y<n:
            if mapp[x][y] == 0 and mapp[x-1][y] == 0 and mapp[x][y-1] == 0:
                dfs([x, y], 2)
        x -= 1
        y -= 1
        #아래로
        x += 1
        if x < n:
            if mapp[x][y] == 0:
                dfs([x, y], 3)
        x -= 1

    if dir == 3 :
        # 오른쪽아래로        
        x += 1
        y += 1
        if x<n and y<n:
            if mapp[x][y] == 0 and mapp[x-1][y] == 0 and mapp[x][y-1] == 0:
                dfs([x, y], 2)
        x -= 1
        y -= 1
        #아래로
        x += 1
        if x < n:
            if mapp[x][y] == 0:
                dfs([x, y], 3)
        x -= 1


dfs((0, 1), 1)
print(cnt)
