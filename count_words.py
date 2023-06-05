s=list(input().lower().split())
c=0
for i in s:
    if (i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o' or i[0]=='u') and (i[-1]!='a' and i[-1]!='e' and i[-1]!='i' and i[-1]!='o' and i[-1]!='u'):
        c=c+1
print(c)
    
        
    
