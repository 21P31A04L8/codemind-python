a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
n1=[]
for i in n:
    if i not in m:
        if i not in n1:
            n1.append(i)
for i in m:
    if i not in n:
        if i not in n1:
            n1.append(i)
print(len(n1))    