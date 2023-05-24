n=int(input())
n1,n2=0,1
c=0
while c<n:
    print(n1,end=' ')
    n3=n1+n2
    n1=n2
    n2=n3
    c=c+1