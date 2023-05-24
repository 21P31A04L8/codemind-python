def p(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
x=int(input())
y=int(input())
s=x+y
i=1
s=s+1
while s>0:
    if p(s):
        print(i)
        break
    i+=1
    s=s+1
    