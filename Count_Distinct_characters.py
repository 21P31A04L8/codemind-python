n=input().lower()
l=[]
for i in n:
    if i!=' ' and i not in l:
        l.append(i)
print(len(l))
        