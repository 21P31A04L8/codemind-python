a,k=map(int,input().split())
l=list(map(int,input().split()))
s=0
s1=0
l1=[]
for i in l:
    c=0
    if i<0:
        i=-i
    if i==0:
        i=1
    while i:
        c=c+1
        i=i//10
    if c==k:
        s=s+1
print(s)