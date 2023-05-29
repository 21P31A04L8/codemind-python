def p(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
def rev(a):
    rn=0
    while a>0:
        r=a%10
        rn=(rn*10)+r
        a=a//10
    return rn
n=int(input())
if p(n):
    if p(rev(n)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    