from collections import defaultdict

n, m, k = map(int, input().split(' '))

s2d2 = []
for i in range(n):
    s2d2.append(list(map(int, input().split(' '))))

trees = []
for i in range(m):
    a, b, c = map(int, input().split(' '))
    trees.append([a-1, b-1, c])

treemap = {}
for i in range(n):
    for j in range(n):
        treemap[(i, j)] = defaultdict(lambda: 0)

for i in trees:
    x, y, z = i
    treemap[(x, y)][z] += 1

yangboonmap = [[5 for _ in range(n)] for _ in range(n)]

year = 0
flag = 0
while (True):
    # 봄 양분 소비, 나이먹기, 죽으면 양분 뿌리기
    for i in range(n):
        for j in range(n):
            next_cell = defaultdict(lambda: 0)
            yangboon = 0
            for age, count in sorted(treemap[(i, j)].items()):  
                #양분 소비하기
                survive = min(yangboonmap[i][j]//age, count)
                #양분을 소비하지 못하는 나무 카운트하기
                dead = count - survive

                if survive > 0:
                    #양분 소비한 만큼 차감하기
                    yangboonmap[i][j] -= age*survive
                    #나이먹을 준비
                    next_cell[age+1] = survive

                #죽은나무 양분뿌리기
                yangboon += (age//2)*dead

            yangboonmap[i][j] += yangboon
            treemap[(i, j)] = next_cell

    
    # 가을은 번식
    for i in range(n):
        for j in range(n):
            for treeage, count in treemap[(i, j)].items():
                if treeage % 5 == 0:
                    for ii in [-1, 0, 1]:
                        for jj in [-1, 0, 1]:
                            if ii == 0 and jj == 0:
                                continue
                            ni = i + ii
                            nj = j + jj
                            if 0 <= ni < n and 0 <= nj < n:
                                if 1 in treemap[(ni, nj)]:
                                    treemap[(ni, nj)][1] += count
                                else:
                                    treemap[(ni, nj)][1] = count


    # 겨울에 양분뿌리기
    for i in range(n):
        for j in range(n):
            yangboonmap[i][j] += s2d2[i][j]

    # 해당 연도에 남은 나무 수 파악하고 끝
    year += 1
    if year == k:
        ans = 0
        for i in range(n):
            for j in range(n):
                for k, v in treemap[(i, j)].items():
                    ans += v
        print(ans)
        break
