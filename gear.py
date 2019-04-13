tob = []
tob.append(list(input()))
tob.append(list(input()))
tob.append(list(input()))
tob.append(list(input()))


rotation_list = [0, 0, 0, 0]
visited = [0, 0, 0, 0]

def rotate(n, d):
    global tob
    if d == 1:
        temp = tob[n].pop()
        tob[n] = [temp] + tob[n] 

    if d == -1:
        temp = tob[n].pop(0)
        tob[n] = tob[n] + [temp] 
    

def dfs(gear, ddd):
    global rotation_list
    global visited
    global top
    if visited[gear] == 1:
        return
    visited[gear] = 1
    rotation_list[gear] = ddd
    if gear + 1 <= 3 and tob[gear][2] != tob[gear+1][-2]:
        dfs(gear+1, ddd*(-1))
    if gear - 1 >= 0 and tob[gear][-2] != tob[gear-1][2]:
        dfs(gear-1, ddd*(-1))


# dfs(3-1, 1)
# print(rotation_list)
move = []
n= int(input())
for i in range(n):
    move.append(list(map(int, input().split(' '))))

for gear, dd in move:
    rotation_list = [0, 0, 0, 0]
    visited = [0, 0, 0, 0]
    dfs(gear-1, dd)
    for i in range(4):
        rotate(i, rotation_list[i])

score = 0 
for i in range(4):
    if tob[i][0] == '1':
        score += 2**i
print(score)
