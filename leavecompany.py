n = int(input())
work = []
for i in range(n):
    work.append(list(map(int, input().split(' '))))

ans = 0
cnt = 0
def dfs(day, pay, temp):
    global ans
    global cnt
    if day == n:
        ans = max(ans, pay)
    if day > n:
        ans = max(ans, temp)
        return
        
    for i in range(day ,n):
        dfs(i+work[i][0], pay+work[i][1], pay)
            
dfs(0, 0, 0)
print(ans)
