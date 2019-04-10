n = int(input())

curve = []
for i in range(n):
    curve.append(list(map(int, input().split(' '))))

size = 101
mapp = [[0 for _ in range(size)] for _ in range(size)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dragon(start):
    global mapp
    x, y, d, g = start

    l = [d]
    for i in range(g):
        l += [ (i+1)%4 for i in reversed(l) ]

    mapp[x][y] = 1
    for i in l:
        
        x += dx[i]
        y += dy[i]
        mapp[x][y] = 1
    

for i in curve:
    dragon(i)

cnt = 0
for i in range(size-1):
    for j in range(size-1):
        if mapp[i][j] and mapp[i+1][j] and mapp[i][j+1] and mapp[i+1][j+1]:
            cnt += 1

print(cnt)
