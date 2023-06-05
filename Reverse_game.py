n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    
    c=0
    while i:
        c=c*10+i%10
        i=i//10
    l1.append(c)
for i in l1:
    print(i,end=' ')