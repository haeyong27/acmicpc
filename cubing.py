color = ['w', 'y', 'r', 'o', 'g', 'b']

u = [color[0] for _ in range(9)]
d = [color[1] for _ in range(9)]
f = [color[2] for _ in range(9)]
b = [color[3] for _ in range(9)]
l = [color[4] for _ in range(9)]
r = [color[5] for _ in range(9)]
test = [i for i in range(9)]

def clock(mapp):
    # 1 - 3 - 7 - 5
    # 0 - 6 - 8 - 2
    mapp[1], mapp[3], mapp[7], mapp[5] = mapp[5], mapp[1], mapp[3], mapp[7]
    mapp[0], mapp[6], mapp[8], mapp[2] = mapp[2], mapp[0], mapp[6], mapp[8]



def rotate(s):
    if s== 'L-':
        #L-
        for i in [0, 3, 6]:
            #u b d f
            u[i], b[i], d[i], f[i] = f[i], u[i], b[i], d[i]
        clock(l)

    if s== 'L+':
        #L-
        for _ in range(3):
            for i in [0, 3, 6]:
                #u b d f
                u[i], b[i], d[i], f[i] = f[i], u[i], b[i], d[i]
            clock(l)

    if s== 'R-':
        #R
        for i in [2, 5, 8]:
            #u f d b 
            u[i], f[i], d[i], b[i] = b[i], u[i], f[i], d[i]
        clock(r)

    if s== 'R+':
        #R
        for _ in range(3):
            for i in [2, 5, 8]:
                #u f d b 
                u[i], f[i], d[i], b[i] = b[i], u[i], f[i], d[i]
            clock(r)

    
    if s== 'F-':
        #F
        for i in [6, 7, 8]:
            #u l d r
            u[i], l[i], d[i*(-1)+8], r[i] = r[i], u[i], l[i], d[i*(-1)+8]
        clock(f)
    if s== 'F+':
        #F
        for _ in range(3):
            for i in [6, 7, 8]:
                #u l d r
                u[i], l[i], d[i*(-1)+8], r[i] = r[i], u[i], l[i], d[i*(-1)+8]
            clock(f)

    if s== 'B-':
    #B
        for i in [0, 1, 2]:
            #b r d l 
            u[i], r[i], d[i*(-1)+8], l[i] = l[i], u[i], r[i], d[i*(-1)+8]
        clock(b)

    if s== 'B+':
        #B
        for _ in range(3):
            for i in [0, 1, 2]:
                #u r d l 
                u[i], r[i], d[i*(-1)+8], l[i] = l[i], u[i], r[i], d[i*(-1)+8]
            clock(b)

    if s== 'U-':
        #U
        for i in range(3):
            #frbl
            f[i], r[i*(-3)+6], b[i*(-1)+8], l[3*i+2] = l[3*i+2], f[i], r[i*(-3)+6], b[i*(-1)+8]
        clock(u)


    if s== 'U+':
        #U
        for _ in range(3):
            for i in range(3):
                f[i], r[i*(-3)+6], b[i*(-1)+8], l[3*i+2] = l[3*i+2], f[i], r[i*(-3)+6], b[i*(-1)+8]
            clock(u)


    if s== 'D-':
        #D
        for i in range(3):
            #flbr
            f[i+6], l[3*i], b[2-i], r[(-3)*i+8] = r[(-3)*i+8], f[i+6], l[3*i], b[2-i]
        clock(d)

    if s== 'D+':
        #D
        for _ in range(3):
            for i in range(3):
                #b r f l
                f[i+6], l[3*i], b[2-i], r[(-3)*i+8] = r[(-3)*i+8], f[i+6], l[3*i], b[2-i]
            clock(d)
        #D

t = int(input())
for tc in range(t):
    n = int(input())
    sss = input().split(' ')

    u = [color[0] for _ in range(9)]
    d = [color[1] for _ in range(9)]
    f = [color[2] for _ in range(9)]
    b = [color[3] for _ in range(9)]
    l = [color[4] for _ in range(9)]
    r = [color[5] for _ in range(9)]

    for i in sss:
        rotate(i)

    # ans = []
    # ans.append(u[0]+u[1]+u[2])
    # ans.append(u[3]+u[4]+u[5])
    # ans.append(u[6]+u[7]+u[8])
    # for i in ans:
    #     print(i)

    for i in range(3):
        print("".join(u[3*i:3*i+3]))
