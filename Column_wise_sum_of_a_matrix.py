r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
for i in range(c):
    sum=0
    for j in range(r):
        sum=sum+mat[j][i]
    print(sum,end=" ")