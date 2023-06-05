a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=0
c1=[]
for i in l1:
    if i in l2:
        if i not in c1:
            c1.append(i)
print(len(c1))