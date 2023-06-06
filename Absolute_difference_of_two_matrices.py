n=int(input())
a=[]
b=[]
c=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s)
for i in range(n):
    s=list(map(int,input().split()))
    b.append(s)
for i in range(n):
    s=[]
    for j in range(n):
        s.append(abs(a[i][j]-b[i][j]))
    c.append(s)
for i in c:
    print(*i)