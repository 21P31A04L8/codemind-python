a=input().lower()
b=input().lower()
a1=list(a.split())
a2=list(b.split())
c=0
for i in a1:
    if i in a2:
        c=c+1
print(c)
    