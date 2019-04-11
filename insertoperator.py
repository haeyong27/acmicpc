n = int(input())
ss = list(map(int , input().split(' ')))
op = list(map(int, input().split(' ')))

a,b,c,d = op
M = -10**9
m = 10**9
def dfs(i, r, a, b, c, d):
    global M, m
    if n == i:
        M = max(M, r)
        m = min(m, r)
        return    
    if a: dfs(i+1, r+ss[i], a-1, b, c, d)
    if b: dfs(i+1, r-ss[i], a, b-1, c, d)
    if c: dfs(i+1, r*ss[i], a, b, c-1, d)
    if d: dfs(i+1, int(r/ss[i]), a, b, c, d-1)

dfs(1, ss[0], a, b, c, d)
print(M)
print(m)
