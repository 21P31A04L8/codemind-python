n=int(input())
l=list(map(int,input().split()))
k=int(input())
c1=0
for i in l:
    c=0
    for j in range(2,i):
        if i%j==0:
            c=c+1
    if i<=k and i>1 and c==0:
        c1=c1+1
print(c1)