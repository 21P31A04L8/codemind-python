s=input()
n=list(s)
#print(n)
l1=[]
c=0
for i in n:#education 
    if i not in l1:
        l1.append(i)
    else:
        c=c+1
if c==0:
    print("True")
else:
    print("False")