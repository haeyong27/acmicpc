n, l = map(int, input().split(' '))
mapp = []
for i in range(n):
    mapp.append(list(map(int, input().split(' '))))


ans = 0
#가로탐색
def solution():
    global ans
    global mapp
    for i in range(n):
        temp = mapp[i][0]
        cnt = 1
        for j in range(1, n):
            if abs(temp - mapp[i][j]) > 1:
                break
            if j == n-1: #마지막칸
                if temp == mapp[i][j]:
                    ans += 1
                elif mapp[i][j] - temp == 1:
                    if cnt >= l:
                        ans += 1
                elif temp - mapp[i][j] == 1:
                    if l == 1:
                        ans += 1
                continue
            #같을 때
            if temp == mapp[i][j]:
                cnt +=1
                temp = mapp[i][j]
                continue

            elif mapp[i][j] - temp == 1:
                #이전보다 높으면

                temp = mapp[i][j]
                if cnt >= l:
                    cnt = 1
                else:
                    break

            elif temp - mapp[i][j] == 1:
                #이전보다 낮으면
                cnt = 1
                temp = mapp[i][j]
                #가능성이 있으면 내려갈 수 있는지 체크하기
                if j+l-1 < n:
                    flag = 0
                    for ii in range(1, l):
                        if mapp[i][j+ii] != mapp[i][j]:
                            flag = 1
                            break
                    if flag == 1:
                        break
                    elif flag == 0:
                        cnt = -l + 1
                else:
                    break

solution()
for i in range(n):
    for j in range(n):
        if i < j:
            mapp[i][j], mapp[j][i] = mapp[j][i], mapp[i][j]
solution()

print(ans)
