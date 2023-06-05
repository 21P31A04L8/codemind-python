s1=input().lower()
s2=input().lower()
l=list(set(s1)&set(s2))
c=0
for i in l:
    if i!=' ' and i.isalpha():
        c=c+1
print(c)