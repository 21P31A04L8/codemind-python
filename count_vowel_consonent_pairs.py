s=list(input().lower())
c=0
for i in range(len(s)):
    if (s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u' and s[i]!=' ') and(s[-i-1]=='a' or s[-i-1]=='e' or s[-i-1]=='i' or s[-i-1]=='o' or s[-i-1]=='u'):
        c=c+1
print(c)