'''
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N – 1, N – 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are ‘U'(up), ‘D'(down), ‘L’ (left), ‘R’ (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it. Return the list of paths in lexicographically increasing order.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.
'''


N=int(input())
a=[]
for i in range(N):
    t=input().split(' ')
    a.append( [int(k) for k in t])

p=[]
s=(0,0)
e=(N-1,N-1)

def check(a):
    if len(a) < 2:
        return False
    i,j = a[-1]
    k,l = a[-2]

    if (i==k) or (j==l):
        return False
    return True

def P_ways(r):
    global N,p,s,e,a
    i,j=r[-1]
    root = [k for k in r]
    
    if check(root):
        return

    if (i,j) == e:
        p.append(root)
        return
    
    if i+1 <N and a[i+1][j]==1 and ((i+1,j) not in root):
        root.append((i+1,j))
        P_ways(root)
        root.pop()

    if j+1 <N and a[i][j+1]==1 and ((i,j+1) not in root) :
        root.append((i,j+1))
        P_ways(root)
        root.pop()

    if not(i ==0 ) and a[i-1][j]==1 and ((i-1,j) not in root):
        root.append((i-1,j))
        P_ways(root)
        root.pop()

    if not(j ==0 ) and a[i][j-1]==1 and ((i,j-1) not in root):
        root.append((i,j-1))
        P_ways(root)
        root.pop()
    return


def cov(a):
    s=''
    for t in range(1,len(a)):
        i,j = a[t-1]
        k,l = a[t]

        if (k,l)== (i,j+1):
            s+='R '
        if (k,l)== (i,j-1):
            s+='L '
        if (k,l)== (i+1,j):
            s+='D '
        if (k,l)== (i-1,j):
            s+='U '
    return s
P_ways([s])
for i in p:
    print(cov(i))
