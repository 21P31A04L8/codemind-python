n=input()
l=[]
for i in n:
    if i not in ' ':
        l.append(i)
print(len(l))