r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
max=0
for i in range(r):
    sum=0
    for j in range(c):
        sum=sum+mat[i][j]
    if sum>max:
        max=sum
print(max)