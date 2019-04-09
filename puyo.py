mapp = []
for i in range(12):
    mapp.append(list(input()))
check = [[0 for _ in range(6)] for _ in range(12)]
ans = 0

def delete(loc):
    global mapp
    global check
    global ans
    x, y = loc
    color = mapp[x][y]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    stack = [loc]
    delete_list = []
    cnt = 0
    while(stack):
        x, y = stack.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<12 and 0<=ny<6 and check[nx][ny] == 0 and mapp[nx][ny] == color:
                check[nx][ny] = 1
                delete_list.append((nx, ny))
                stack.append((nx, ny))
                cnt += 1
    if cnt >= 4:
        return delete_list
    else:
        return []


def find_delete():
    global mapp
    global check
    global ans
    flag = 0
    for i in range(12):
        for j in range(6):
            if mapp[i][j] != '.':
                check = [[0 for _ in range(6)] for _ in range(12)]
                for x, y in delete((i, j)):
                    mapp[x][y] = '.'
                    flag = 1
    if flag == 1:
        ans += 1
    return flag

def move_down():
    global mapp
    temp_list1 = []
    for j in range(6):
        temp_list2 = []
        for i in range(12):
            if mapp[i][j] != '.':
                temp_list2 += [mapp[i][j]]
        temp_list1.append(temp_list2)

    mapp = [['.' for _ in range(6)] for _ in range(12)]

    for col_i, col_list in enumerate(temp_list1):
        for i in range(12-len(col_list), 12):
            mapp[i][col_i] = col_list.pop(0)



while(True):
    if find_delete():
        move_down()
    else:
        break

print(ans)
