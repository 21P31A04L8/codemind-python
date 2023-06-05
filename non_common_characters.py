s1=input().lower()
s2=input().lower()
s1=set(s1)
s2=set(s2)
s1.discard(' ')
s2.discard(' ')
a=s1.symmetric_difference(s2)
l1=[]
for i in a:
    if i!=" " and i.isalpha():
        l1.append(i)
l1.sort()
print("".join(l1))