def p(n,m):
    c=0
    for i in range(n,m+1):
        if i>1:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                c=c+1
    print(c)
n=int(input())
m=int(input())
p(n,m)