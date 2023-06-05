n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    c=0
    for j in range(2,i):
        if i%j==0:
            c=c+1
    if i>1 and i!=0 and c==0:
        p.append(i)
s=sum(p)
s1=len(p)
r=s/s1
print('{:.2f}'.format(r))