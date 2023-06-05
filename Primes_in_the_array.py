n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    c=0
    for j in range(2,i):
        if i%j==0:
            c=c+1
    if c==0 and i>=2:
        s=s+1
print(s)