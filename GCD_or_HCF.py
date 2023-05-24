def gcd(a,b):#12 18 (12,6) 
    while b:#18(it is true then it go to next step)
        if a>b:#12<18(it is true it go to the b%a)
            a,b=b,a#(6,12)
        b=b%a#6
    return a
a,b=map(int,input().split())
print (gcd(a,b))
