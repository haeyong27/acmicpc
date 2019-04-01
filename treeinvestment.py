# n, m, k = map(int, input().split(' '))

# mapp = []
# for i in range(n):
#     mapp.append(list(map(int, input().split(' '))))

# trees = []
# for i in range(m):
#     trees.append(map(int, input().split(' ')))

n, m, k = (5, 2, 1)
s='''2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2'''

mapp = []
for i in s.split('\n'):
    mapp.append(list(map(int, i.split(' '))))

for i in range(n):
    for j in range(n):
        mapp[i][j] += 5

trees = [[2, 1, 3], [3, 2, 3]]

tmap = [[[0] for _ in range(n)] for _ in range(n)]

for i in trees:
    x, y, z = i
    tmap[x][y] = [z]

year = 0
def add(a):
    return a+1
    
while(True):
    year += 1
    #양분 소비
    for i in range(n):
        for j in range(n):
            mapp[i][j] -= tmap[i][j][0]
    #나이 한살 먹기
    for i in trees:
        i[2] += 1
    
    #한살 먹은 나무들 나이 갱신
    for i in trees:
        x, y, z = i
        tmap[x][y] = [z]

    #해당 연도에 남은 나무 수 파악하고 끝
    if year == k:
        print('answer')
        break
