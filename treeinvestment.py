n, m, k = map(int, input().split(' '))

s2d2 = []
for i in range(n):
    s2d2.append(list(map(int, input().split(' '))))

trees = []
for i in range(m):
    a, b, c = map(int, input().split(' '))
    trees.append([a-1, b-1, c])

yangboonmap = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        yangboonmap[i][j] += 5

treemap = [[[] for _ in range(n)] for _ in range(n)]
for i in trees:
    x, y, z = i
    treemap[x][y].append(z)
year = 0
flag = 0
while (True):
    treetokill = []
    # 봄
    # 양분 소비
    for i in range(n):
        for j in range(n):
            if treemap[i][j]:
                for treeage in sorted(treemap[i][j]):
                    if yangboonmap[i][j] - treeage >= 0:
                        yangboonmap[i][j] -= treeage
                    else:  
                        #양분을 소비하지 못하는 나무의 좌표와 나이
                        treetokill.append((i, j, treeage))


    # 여름은 죽을 나무가 죽고, 양분이 되기
    for i, j, c in treetokill:
        treemap[i][j].remove(c)
        yangboonmap[i][j] += int(c/2)


    # 나이 한살 먹기
    for i in range(n):
        for j in range(n):
            if treemap[i][j]:
                treemap[i][j] = [a + 1 for a in treemap[i][j]]





    # if (year+1)==k:
    #     ans = 0
    #     flag = 1   
    #     for i in range(n):
    #         for j in range(n):
    #             ans += len(treemap[i][j])

    #     # 가을은 번식
    #     for i in range(n):
    #         for j in range(n):
    #             if treemap[i][j]:
    #                 for treeage in sorted(treemap[i][j]):
    #                     if treeage % 5 == 0:
    #                         for ii in [-1, 0, 1]:
    #                             for jj in [-1, 0, 1]:
    #                                 if ii == 0 and jj == 0:
    #                                     continue
    #                                 ni = i + ii
    #                                 nj = j + jj
    #                                 if 0 <= ni < n and 0 <= nj < n:
    #                                     ans += 1
        

    if flag == 1:
        print(ans)
        break
    # 가을은 번식
    for i in range(n):
        for j in range(n):
            if treemap[i][j]:
                for treeage in sorted(treemap[i][j]):
                    if treeage % 5 == 0:
                        for ii in [-1, 0, 1]:
                            for jj in [-1, 0, 1]:
                                if ii == 0 and jj == 0:
                                    continue
                                ni = i + ii
                                nj = j + jj
                                if 0 <= ni < n and 0 <= nj < n:
                                    treemap[ni][nj].append(1)

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
                ans += len(treemap[i][j])
        print(ans)
        break
