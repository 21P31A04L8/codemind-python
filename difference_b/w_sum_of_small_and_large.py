n=list(input().lower().split())
m=[]
s=[]
for i in n:
    m1=ord(max(i))
    s1=ord(min(i))
    m.append(m1)
    s.append(s1)
print(sum(m)-sum(s))