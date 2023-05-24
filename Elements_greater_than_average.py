n=int(input())
l=list(map(int,input().split()))
k=sum(l)//len(l)
c=0
for i in range(n):
    if l[i]>=k:
        c=c+1
print(c)
        