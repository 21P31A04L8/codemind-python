n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    c=c+l[i]*2**(n-i-1)
print(c)