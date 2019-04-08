mapp = []
for i in range(10):
    mapp.append(list(map(int, input().split(' '))))

def fill(loc, size):
    global mapp
    x, y = loc
    for i in range(x, x+size):
        for j in range(y, y+size):
            if 0<=i<10 and 0<=j<10:
                if mapp[i][j] == 0:
                    return False
            else:
                return False

    for i in range(x, x+size):
        for j in range(y, y+size):
            mapp[i][j] = 0

    return size

def check_complete():
    global mapp
    for i in range(10):
        if 1 in mapp[i]:
            return False
    return True

def find_loc():
    global mapp
    for i in range(10):
        for j in range(10):
            if mapp[i][j] == 1:
                return (i, j)

def fill_restore(loc, filledi):
    global mapp
    x, y = loc
    for i in range(x, x+filledi):
        for j in range(y, y+filledi):
            mapp[i][j] = 1

def dfs():
    global mapp
    global ans
    #색종이를 삽입할 위치를 찾고
    x, y = find_loc()
    #큰것부터 차례로 넣어본다.
    for size in reversed(range(1, 6)):
        if cnt[size] < 5:
            result = fill([x, y], size)
            if result:
                cnt[size] += 1
                #넣은 뒤 다 채워졌는지 확인
                #다 채워졌으면 ans 갱신하기
                if check_complete():
                    tot_cnt = 0
                    for c in cnt:
                        tot_cnt += c
                    ans = min(ans, tot_cnt)
                    fill_restore([x, y], size)
                    cnt[size] -= 1
                    return
                #다음 색종이 채우기
                dfs()
                fill_restore([x, y], size)
                cnt[size] -= 1

#색종이를 붙이기전에 모두 채워져있으면 0 출력
if check_complete():
    print(0)

else:
    cnt = [0 for _ in range(6)]
    ans = 1000
    dfs()
    #정답이 갱신되지 않았으면 채우기 불가능한 경우이므로 -1 출력
    if ans == 1000:
        print(-1)
    else:
        print(ans)
