n=int(input())
l=len(str(n))
t=n
s=0
r=0
while t>0:
    r=t%10
    s=s+int(r**l)
    t=t//10
    l=l-1
if s==n:
    print(True)
else:
    print(False)