n = 5
s = '''4 4 0 0 1
4 4 4 0 1
8 8 8 8 1
1 2 4 8 8
2 2 2 2 2'''
mapp = []

for i in s.split('\n'):
    mapp.append(list(map(int, i.split(' '))))


#위
for j in range(n):
    temp = mapp[0][j]
    for i in range(1, n):
        if mapp[i][j] == 0:
            continue
        if temp == mapp[i][j]:
            mapp[i][j] = 0
            mapp[i-1][j] *= 2
        temp = mapp[i][j]

for i in mapp:
    print(i)

for j in range(n):
    idx = 0
    for i in range(n):
        if mapp[i][j] != 0:
            temp = mapp[i][j]
            mapp[i][j] = 0
            mapp[idx][j] = temp 
            idx += 1

print()
for i in mapp:
    print(i)




#왼
for l in mapp:
    temp = [i for i in l if i != 0]
    for i in range(len(temp)-1):
        if temp[i] == 0:
            continue
        if temp[i] == temp[i+1]:
            temp[i] *= 2
            temp[i+1] = 0
    temp_map = [i for i in temp if i != 0]
    print(temp_map)

#오
for l in mapp:
    temp = [i for i in reversed(l) if i != 0]
    for i in range(len(temp)-1):
        if temp[i] == 0:
            continue
        if temp[i] == temp[i+1]:
            temp[i] *= 2
            temp[i+1] = 0
    temp_map = [i for i in reversed(temp) if i != 0]
    print(temp_map)

