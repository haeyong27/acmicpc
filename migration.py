n, dif1, dif2 = map(int, input().split(' '))

mapp = []
for i in range(n):
    mapp.append(list(map(int, input().split(' '))))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

check = []
group = [] 


def bfs(x, y, idx):
    global mapp
    global check
    global group
    
    stack = [(x, y)]
    check[x][y] = 1 
    group[x][y] = idx
    while(stack):
        x, y = stack.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and check[nx][ny] == 0 and dif1 <= abs(mapp[x][y] - mapp[nx][ny]) <= dif2:
                check[nx][ny] = 1
                stack.append((nx, ny))
                group[nx][ny] = idx


def solution():
    global mapp
    global check
    global group
    ans = 0
    while(True):
        
        check = [[0 for _ in range(n)] for _ in range(n)]
        group = [[0 for _ in range(n)] for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(n):
                if check[i][j] == 0:
                    idx += 1
                    bfs(i, j, idx)
            
        #idx는 그룹의 수이다. 각 그룹의 합을 구하기
        group_sum = [0 for _ in range(idx+1)]
        group_count = [0 for _ in range(idx+1)]
        for i in range(n):
            for j in range(n):
                group_sum[group[i][j]] += mapp[i][j]
                group_count[group[i][j]] += 1

        for i in range(n):
            for j in range(n):
                mapp[i][j] = int(group_sum[group[i][j]]/group_count[group[i][j]])

        if idx == n*n:
            return ans
        ans += 1

print(solution())
