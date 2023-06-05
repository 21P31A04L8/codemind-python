n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
a=[]
for i in l:
    if i%k!=0:
        a.append(i)
print(len(a))

