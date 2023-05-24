n=int(input())#12
n1=n**2#144
s=str(n)#'12'
r=int(s[::-1])#21
r1=r**2#441
s1=str(r1)
r2=int(s1[::-1])
if n1==r2:
    print("True")
else:
    print("False")