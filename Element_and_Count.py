n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i not in k:
        k.append(i)
        print(i,end=' ')
        print(l.count(i),end=' ')