s1=input().lower()
s2=input().lower()
l=list(set(s1)&set(s2))
l2=[]
for i in l:
    if i!=' ' and i.isalpha():
        l2.append(i)
l2.sort()
if len(l2)==0:
    print("-1")
else:
    print("".join(l2))