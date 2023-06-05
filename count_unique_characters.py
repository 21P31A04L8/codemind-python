n=input().lower()
c=0
for i in n:
    if i!=' ' and n.count(i)==1:
        c=c+1
print(c)