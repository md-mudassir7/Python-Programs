def fun(l,m,dp):
    if m==0:
        return 0
    res=2147483647
    for i in range(len(l)):
        if (m-l[i])>=0:
            sub=0
            if dp[m-l[i]]!=-1:
                sub=dp[m-l[i]]
            else:
                sub=fun(l,m-l[i],dp)
            if sub!=2147483647 and sub+1<res:
                res=sub+1
    dp[m]=res
    return dp[m]



t=int(input())
for _ in range(t):
    n,m=input().split()
    m=int(n)
    l=list(map(int,input().split()))
    dp=[-1 for x in range(m+1)]
    print(fun(l,m,dp))
