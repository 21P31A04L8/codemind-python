n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
sum=0
for i in range(n):
    for j in range(m):
        if i==j:
            sum=sum+mat[i][j]
        elif i+j==n-1:
            sum=sum+mat[i][j]
print(sum)