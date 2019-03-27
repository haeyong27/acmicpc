mapp = []
for _ in range(5):
    mapp.append(list(input()))

n = 5
m = 9

check = [0 for _ in range(12)]
cnt = 0
loc = []
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 'x':
            cnt += 1
            loc.append((i, j))
            mapp[i][j] = 0
        elif ord('A') <= ord(mapp[i][j]) <= ord('L'):
            num = ord(mapp[i][j]) - ord('A')
            check[num] = 1
            mapp[i][j] = num + 1
        else:
            mapp[i][j] = -1

flag = 0

def dfs(a):
    global flag
    global check

    if (a == cnt):
        if (int(mapp[1][1]) + int(mapp[1][3]) + int(mapp[1][5]) + int(mapp[1][7]) != 26):
            return
        if (int(mapp[0][4]) + int(mapp[1][3]) + int(mapp[2][2]) + int(mapp[3][1]) != 26):
            return
        if (int(mapp[0][4]) + int(mapp[1][5]) + int(mapp[2][6]) + int(mapp[3][7]) != 26):
            return
        if (int(mapp[3][1]) + int(mapp[3][3]) + int(mapp[3][5]) + int(mapp[3][7]) != 26):
            return
        if (int(mapp[1][1]) + int(mapp[2][2]) + int(mapp[3][3]) + int(mapp[4][4]) != 26): 
            return
        if (int(mapp[1][7]) + int(mapp[2][6]) + int(mapp[3][5]) + int(mapp[4][4]) != 26): 
            return
        flag = 1
        return

    for i in range(12):

        if check[i] == 1:
            continue
        check[i] = 1
        mapp[loc[a][0]][loc[a][1]] = i + 1
 

        if (4<a<8) and (int(mapp[1][1]) + int(mapp[1][3]) + int(mapp[1][5]) + int(mapp[1][7]) != 26):
            check[i] = 0
            mapp[loc[a][0]][loc[a][1]] = 0
            continue

        elif (a>7) and (int(mapp[0][4]) + int(mapp[1][3]) + int(mapp[2][2]) + int(mapp[3][1]) != 26):
            check[i] = 0
            mapp[loc[a][0]][loc[a][1]] = 0
            continue
            
        # elif (a>10) and ((int(mapp[0][4]) + int(mapp[1][5]) + int(mapp[2][6]) + int(mapp[3][7]) != 26) or (int(mapp[3][1]) + int(mapp[3][3]) + int(mapp[3][5]) + int(mapp[3][7]) != 26)):
        #     check[i] = 0
        #     mapp[loc[a][0]][loc[a][1]] = 0
        #     continue

        dfs(a+1)

        if flag == 1:
            return
            
        mapp[loc[a][0]][loc[a][1]] = 0
        check[i] = 0

dfs(0)

for i in range(n):
    for j in range(m):
        if type(mapp[i][j]) == type(1):
            if 1 <= mapp[i][j] <= 12:
                mapp[i][j] = chr(64+mapp[i][j])
            elif mapp[i][j] < 1:
                mapp[i][j] = '.'

for i in mapp:
    print(''.join(i))
