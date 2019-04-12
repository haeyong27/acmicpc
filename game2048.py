n = int(input())

ori_map = []
for i in range(n):
    ori_map.append(list(map(int, input().split(' '))))

ans = 0
def dfs(mapp, cnt, d):
    global ans
    if cnt == n:
        for i in mapp:
            result = max(i)
            ans = max(ans, result)
        return

    if d == 0:
        #왼쪽으로 기울기
        for i in range(n):
            temp = mapp[i][0]
            idx = 0
            for j in range(1, n):
                if mapp[i][j] == 0:
                    continue
                if temp == mapp[i][j]:
                    mapp[i][idx] = temp*2
                    temp = 0
                    mapp[i][j] = 0
                    idx += 1
                else:
                    mapp[i][idx] = temp
                    idx += 1
                    temp = mapp[i][j]

        
        for i in range(n):
            idx = 0
            for j in range(n):
                if mapp[i][j] != 0:
                    temp = mapp[i][j]
                    mapp[i][j] = 0
                    mapp[i][idx] = temp
                    idx += 1

        for i in range(4):
            dfs(mapp, cnt+1, i)

    if d == 1:
        #왼쪽으로 기울기
        for i in range(n):
            temp = mapp[i][n-1]
            idx = n-1
            for j in reversed(range(n-1)):
                if mapp[i][j] == 0:
                    continue
                if temp == mapp[i][j]:
                    mapp[i][idx] = temp*2
                    temp = 0
                    mapp[i][j] = 0
                    idx -= 1
                else:
                    mapp[i][idx] = temp
                    idx -= 1
                    temp = mapp[i][j]


        for i in range(n):
            idx = n-1
            for j in reversed(range(n)):
                if mapp[i][j] != 0:
                    temp = mapp[i][j]
                    mapp[i][j] = 0
                    mapp[i][idx] = temp
                    idx -= 1
        for i in range(4):
            dfs(mapp, cnt+1, i)

    if d == 2:
        
        for j in range(n):
            temp = mapp[0][j]
            idx = 0 
            for i in range(1, n):
                if mapp[i][j] == 0:
                    continue
                if mapp[i][j] == temp:
                    mapp[idx][j] = temp*2
                    idx += 1
                    mapp[i][j] = 0
                    temp = 0
                else:
                    mapp[idx][j] = temp
                    temp = mapp[i][j]
                    idx += 1

        for j in range(n):
            idx = 0
            for i in range(n):
                if mapp[i][j] != 0:
                    temp = mapp[i][j]
                    mapp[i][j] = 0
                    mapp[idx][j] = temp
                    idx+=1

        for i in range(4):
            dfs(mapp, cnt+1, i)

    if d == 3:
        for j in range(n):
            temp = mapp[n-1][j]
            idx = n-1
            for i in reversed(range(n-1)):
                if mapp[i][j] == 0:
                    continue
                if mapp[i][j] == temp:
                    mapp[idx][j] = temp*2
                    idx -= 1
                    mapp[i][j] = 0
                    temp = 0
                else:
                    mapp[idx][j] = temp
                    temp = mapp[i][j]
                    idx -= 1


        for j in range(n):
            idx = n-1
            for i in reversed(range(n)):
                if mapp[i][j] != 0:
                    temp = mapp[i][j]
                    mapp[i][j] = 0
                    mapp[idx][j] = temp
                    idx-=1

        for i in range(4):
            dfs(mapp, cnt+1, i)

            
for i in range(4):
    dfs(ori_map, 0, i)
print(ans)
