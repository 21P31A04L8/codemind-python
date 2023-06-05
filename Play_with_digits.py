n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    while i:
        s=s+i%10
        
        i=i//10
print(s)