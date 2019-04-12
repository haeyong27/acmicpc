n = int(input())
mapp = list(map(int, input().split(' ')))
b, c = map(int, input().split(' '))
sum = n
for i in range(len(mapp)):
    mapp[i] -= b
    if mapp[i] < 0:
        continue
    if mapp[i] % c == 0:
        sum += mapp[i] // c
    else:
        sum += mapp[i] // c + 1

print(sum)
