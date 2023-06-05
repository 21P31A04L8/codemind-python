n=int(input())
l=list(map(int,input().split()))
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
    l1.append(c)
#print(l1)
a=max(l1)
print(l1.count(a))