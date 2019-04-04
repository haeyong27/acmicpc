n, m = map(int, input().split(' '))

mapp = []
for i in range(n):
    mapp.append(list(map(int, input().split(' '))))

house_list = []
chicken_house_list = []

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1:
            house_list.append((i,j))
        elif mapp[i][j] == 2:
            chicken_house_list.append((i, j))
            mapp[i][j] = 0

answer = 99999
check = [0 for _ in range(len(chicken_house_list))]
temp = []
min_dist = 99999

def dfs(idx, cnt):
    global min_dist
    if cnt == m:
        total_dist = 0
        for x, y in house_list:
            chick_dist = 9999
            for a, b in temp:
                chick_dist = min(chick_dist, abs(a-x) + abs(b-y))
            total_dist += chick_dist
        min_dist = min(total_dist, min_dist)
        return

    for i in range(idx, len(chicken_house_list)):
        if check[i] == 1:
            continue
        check[i] = 1
        temp.append(chicken_house_list[i])
        dfs(i, cnt+1)
        temp.pop()
        check[i]=0

dfs(0, 0)
print(min_dist)
