


s=input()
n=len(s)+1
s1=s[::-1]
dp = [[0 for _ in range(n)] for _ in range(n)]
res=1
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            dp[i][j]=0
        elif s[i-1]==s[n-j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            res=max(res,dp[i][j])
            

        else:
            dp[i][j]=0

print(res)
