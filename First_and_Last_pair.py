n=int(input())
l=list(map(int,input().split()))
if n%2!=0:
    l.insert(n//2+1,0)
l1=l[:len(l)//2]
l2=l[len(l)//2:]
l2=l2[::-1]
k=[]
for i in range(len(l1)):
    k.append(l1[i])
    k.append(l2[i])
print(*k)