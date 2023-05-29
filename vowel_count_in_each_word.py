def fun(n):
    c=0
    for i in n:
        if i in 'aeiou':
            c=c+1
    return c
n=list(input().lower().split())
l=[]
for i in n:
    l.append(fun(i))
print(*l)
        