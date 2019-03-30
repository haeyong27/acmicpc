# T = int(input())
# for testcase in range(1, T+1):
#   mapp.append(map(int, list(input().split(' '))))
# 
#     
s ='''4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4'''
n = 4
mapp = []
for i in s.split('\n'):
    mapp.append(list(map(int, i.split(' '))))

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 9:
            shark_loc = (i, j)

print(shark_loc)

#함수를 만들어야하는데 일차적으로는 현재 먹을 수 있는 물고기들의 위치를 가져온다. 
# 먹어야할 마리수를 체크하고 (2마리 라고 가정) 두번 움직인 후 레벨을 올리고 다시 목록을 불러온다.
shark_level = 2
fish = []

def eat():
    pass

def find_fish(level, loc, mapp):
    for i in range(n):
        for j in range(n):
            if mapp[i][j] < level:
                fish.append((i, j))
    # 2개를 먹어야하니까 먹을 2개를 선정
    # 거리따져보고, 조건따져보고 2개 선정하기
    # 그리고 마지막에 먹은 위치를 shark_loc에 대입
    # 움직인 시간 체크하고

    


    
    



