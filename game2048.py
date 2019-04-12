n = int(input())

ori_map = []
for i in range(n):
    ori_map.append(list(map(int, input().split(' '))))

mapp = []

def merge():
    global mapp
    complete_map = []

    for i in mapp:
        # 0제거한 리스트
        temp_list = [item for item in i if item != 0]
        for i in range(1, len(temp_list)):
            if temp_list[i] == temp_list[i-1]:
                temp_list[i-1] *= 2
                temp_list[i] = 0

        temp_list = [item for item in temp_list if item != 0]
        complete_map.append(temp_list[:])
    mapp = []
    for i in complete_map:
        mapp.append(i+[0 for _ in range(n-len(i))])


def leftright():
    global mapp
    for i in mapp:
        i.reverse()


def updown():
    global mapp
    for i in range(n):
        for j in range(n):
            if i<j:
                mapp[i][j], mapp[j][i] = mapp[j][i], mapp[i][j]

def total(d):
    global mapp
    
    #left
    if d==0:
        merge()
    #right
    if d==1:
        leftright()
        merge()
        leftright()
    #up
    if d==2:
        updown()
        merge()
        updown()
    #down
    if d == 3:
        updown()
        leftright()
        merge()
        leftright()
        updown()


ans = 0
temp = []
def dfs(cnt):
    global temp
    global ans
    global mapp
    if cnt == 5:
        mapp = []
        for i in ori_map:
            mapp.append(i[:])

        for i in temp:
            total(i)

        for i in mapp:
            result = max(i)
            ans = max(ans, result)
        return

    for i in range(4):
        temp.append(i)
        dfs(cnt+1)
        temp.pop()

dfs(0)
print(ans)
