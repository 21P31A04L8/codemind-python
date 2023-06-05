s1=input().lower()
s2=input().lower()
s1=set(s1)
s2=set(s2)
s1.discard(' ')
s2.discard(' ')
k=s1.symmetric_difference(s2)
c=0
for i in k:
    if i!=' ' and i.isalpha():
        c=c+1
print(c)