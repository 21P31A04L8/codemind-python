r,c=map(int,input().split())
m=[]
e=0
o=0
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(len(m)):
    if i%2==0:
        e=e+sum(m[i])
for i in range(len(m)):
    if i%2!=0:
        o=o+sum(m[i])
print(e,o)
