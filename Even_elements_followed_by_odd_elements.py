n=int(input())
m=list(map(int,input().split()))
o=e=0
for i in m:
    if i%2==0:
        print(i,end=" ")
for i in m:
    if i%2!=0:
        print(i,end=" ")