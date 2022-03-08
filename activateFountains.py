def fun(l,n):
    dp=[-1]*(n+1)
    for i in range(n):
        left=max(0,i-l[i])
        right=min(n,i+l[i]+1)
        dp[left]=max(dp[left],right)
    print(dp)
    res=1
    right=dp[0]
    nex=-1
    for i in range(n):
        nex=max(nex,dp[i])
        if i==right:
            res+=1
            right=nex
    return res
n=int(input())
l=list(map(int,input().split()))
print(fun(l,n))
