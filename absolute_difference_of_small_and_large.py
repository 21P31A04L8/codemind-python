n=list(input().split())
l=[]
for i in n:
    m=max(i)
    s=min(i)
    r=ord(m)-ord(s)
    l.append(r)
print(*l)
    