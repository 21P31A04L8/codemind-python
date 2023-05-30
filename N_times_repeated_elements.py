n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=[]
d=[]
for i in l:
    if l.count(i)==k:
        if i not in c:
            c.append(i)
if len(c)==0:
    print("-1")
else:
    for i in c:
        print(i,end=' ')