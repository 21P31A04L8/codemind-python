n=input()
c=0
l=0
d=0
s=0
sp=0
for i in n:
    if i.islower():
        l=l+1
    elif i.isupper():
        c=c+1
    elif i.isdigit():
        d=d+1
    elif i in ' ':
        s=s+1
    else:
        sp=sp+1
print(sp)
        
        