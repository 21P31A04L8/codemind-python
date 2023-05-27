n=input()
l=list(n.split())
l1=[]
for i in l:
    l1.append(len(i))
print(min(l1))