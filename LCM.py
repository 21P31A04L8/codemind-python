a,b=map(int,input().split())
if(a>b):
    k=a
else:
    k=b
while(1):
    if(k%a==0 and k%b==0):
        print(k)
        break
    k=k+1