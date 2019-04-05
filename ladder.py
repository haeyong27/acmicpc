n, m, h = map(int, input().split(' '))
mapp  = [[0 for _ in range(n)] for _ in range(h)]


for _ in range(m):
    x, y = map(int, input().split(' '))
    mapp[x-1][y-1] = 1
    mapp[x-1][y] = 1

#다리를 놓을 수 있는 좌표 뽑기
ladder = []
for i in range(h):
    for j in range(n-1):
        if mapp[i][j] == 0 and mapp[i][j+1] == 0:
            ladder.append((i, j))

len_ladder = len(ladder)
ladder_check = [0 for _ in range(len_ladder)]

def check():
    for i in range(n):
        tempi = i
        for idx in range(h):
            if mapp[idx][tempi] == 1 and tempi < n - 1  and mapp[idx][tempi+1] == 1:
                    tempi += 1
            elif mapp[idx][tempi] == 1 and mapp[idx][tempi-1] == 1:
                    tempi -= 1
        if tempi != i:
            return False
    return True


def dfs(idx, cnt, a):
    if cnt == a:
        if check():
            for i in mapp:
                print(i)
            exit()
        return
        
    for i in range(idx, len_ladder):
        if ladder_check[i] == 1:
            continue
        x, y = ladder[i]
        if mapp[x][y] == 1 or mapp[x][y+1] == 1:
            continue
        mapp[x][y] = 1
        mapp[x][y+1] = 1
        ladder_check[i] = 1
        dfs(i, cnt + 1, a)
        mapp[x][y] = 0
        mapp[x][y+1] = 0
        ladder_check[i] = 0

def main():
    for i in [1, 2, 3]:
        dfs(0, 0, i)
    return -1

print(main())

