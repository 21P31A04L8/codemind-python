r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
max=0
for i in range(c):
    sum=0
    for j in range(r):
        sum=sum+mat[j][i]
    if sum>max:
        max=sum
print(max)