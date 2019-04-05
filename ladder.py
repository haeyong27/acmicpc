n, m, h = map(int, input().split(' '))
mapp  = [[0 for _ in range(n*2)] for _ in range(h)]

for _ in range(m):
    x, y = map(int, input().split(' '))
    mapp[x-1][y*2] = 1





def check_map():
    for y in range(1, n*2, 2):
        tempy = y
        for x in range(h):
            if y == 2*(n-1) + 1:
                if mapp[x][y-1] == 1:
                    y -=2
            elif mapp[x][y+1] == 1:
                y += 2
            elif mapp[x][y-1] == 1:
                y -= 2
        if tempy != y:
            return False
    return True

if check_map():
    print(0)
    exit()
#사다리 설치할 수 있는 위치 뽑아내기
install_list = []
for x in range(h):
    for y in range(2,n*2,2):
        if mapp[x][y] == 1:
            continue
        if y == 2*(n-1):
            if mapp[x][y-2] == 1:
                continue
        elif mapp[x][y-2] == 1 or mapp[x][y+2] == 1:
            continue
        install_list.append((x, y))

checklist = [0 for _ in range(len(install_list))]

def dfs(idx, cnt, k):

    if cnt == k:
        if check_map():
            print(k)
            exit()
        return

    for i in range(len(install_list)):
        if checklist[i] == 1:
            continue
        checklist[i] = 1
        x, y = install_list[i]
        mapp[x][y] = 1
        dfs(i, cnt+1, k)
        checklist[i] = 0
        mapp[x][y] = 0

def main():
    for i in [1, 2, 3]:
        dfs(0, 0, i)
    return -1

print(main())
