n=list(input().split())
l=[]
for i in n:
    l.append(i[::-1])
m=l[::-1]
for i in m:
    print(i,end=" ")