n=int(input())
o=[]
l=list(map(int,input().split()))
for i in l:
    if l.count(i)==i:
        if i not in o:
            o.append(i)
if len(o)==0:
    print("-1")
else:
    print(min(o),max(o))