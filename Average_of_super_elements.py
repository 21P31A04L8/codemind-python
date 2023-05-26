n=int(input())
l=list(map(int,input().split()))
k=[]
c=0
for i in l:
    if l.count(i)==i:
        if i not in k:
            k.append(i)
if len(k)==0:
    print(-1)
else:
    print("{:.2f}".format(sum(k)/len(k)))