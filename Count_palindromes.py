n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    d=i
    c=0
    while i:
        c=c*10+i%10
        i=i//10
    if d==c:
        s=s+1
print(s)