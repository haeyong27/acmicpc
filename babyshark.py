# n = int(input()) 
# mapp = []
# for i in range(n):
#     mapp.append(list(map(int, input().split(' '))))

s ='''5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6'''

n = len(s.split('\n'))

mapp = []
for i in s.split('\n'):
    mapp.append(list(map(int, i.split(' '))))

shark_loc = []
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 9:
            shark_loc.append((i, j))
            mapp[i][j] = 0


shark_level = 2
count = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
check = [[0 for _ in range(n)] for _ in range(n)]
dist = [[0 for _ in range(n)] for _ in range(n)]
answer = 0

while(shark_loc):

    flag = 0
    x, y = shark_loc.pop(0)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and shark_level > mapp[nx][ny] and mapp[nx][ny] != 0:
            answer += 1 + dist[x][y]
            check = [[0 for _ in range(n)] for _ in range(n)]
            dist = [[0 for _ in range(n)] for _ in range(n)]
            #잡아먹음
            mapp[nx][ny] = 0
            count += 1
            if shark_level == count:
                shark_level+=1
                count = 0
            #그 장소로 이동 
            #shark_loc에 추가
            #그다음에 다시 처음으로 가기
            shark_loc = [(nx, ny)]
            flag = 1
            break

    if flag == 0:
        for i in range(4):   
            nx = x + dx[i]
            ny = y + dy[i] 
            if 0<=nx<n and 0<=ny<n and (shark_level == mapp[nx][ny] or mapp[nx][ny] == 0) and check[nx][ny] == 0:
                shark_loc.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                check[nx][ny] = 1
    # for i in mapp:
    # print(i)



print(answer)
