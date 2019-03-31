n = int(input())
mapp = []
for i in range(n):
    mapp.append(list(map(int, input().split(' '))))

shark_level = 2
count = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
check = [[0 for _ in range(n)] for _ in range(n)]
dist = [[0 for _ in range(n)] for _ in range(n)]
answer = 0
fish_to_eat = []
limit_dist = 30
flag = 0
shark_loc = []

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 9:
            shark_loc.append((i, j))
            mapp[i][j] = 0
            check[i][j] = 1

while(True):
    #먹을 물고기 찾기
    while(shark_loc):
        x, y = shark_loc.pop(0)
        if dist[x][y] == limit_dist:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and check[nx][ny] == 0:
                #먹는경우
                if shark_level > mapp[nx][ny] and mapp[nx][ny] != 0:
                    
                    check[nx][ny] = 1
                    if flag == 0:
                        limit_dist = dist[x][y] + 1
                        flag = 1
                    fish_to_eat.append((nx, ny))

                #지나가는경우
                elif (shark_level == mapp[nx][ny] or mapp[nx][ny] == 0):
                        dist[nx][ny] = dist[x][y] + 1
                        check[nx][ny] = 1
                        if dist[nx][ny] > limit_dist:
                            continue
                        shark_loc.append((nx, ny))
    #먹을게 없으면 
    if not fish_to_eat:
        break

    #잡아먹기
    tempA = 30
    tempB = 30
    for a, b in fish_to_eat:
        if tempA > a:
            tempA = a
            tempB = b
        elif tempA == a:
            if tempB > b:
                tempA = a
                tempB = b
    
    #옮기고 잡아먹기         
    mapp[tempA][tempB] = 0
    count += 1
    if shark_level == count:
        shark_level+=1
        count = 0
    #상어위치 갱신
    shark_loc = [(tempA, tempB)]
    check[tempA][tempB] = 1

    #이동거리
    answer += limit_dist

    #변수 초기화
    limit_dist = 30
    check = [[0 for _ in range(n)] for _ in range(n)]
    dist = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    fish_to_eat = []

print(answer)
