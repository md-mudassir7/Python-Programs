


def fun(h,l,n):
    if n==1:
        return h[0]
    dp=[0]*n
    dp[0]=h[0]
    dp[1]=max(dp[0]+l[1],h[1],l[0]+l[1])
    for i in range(2,n):
        dp[i]=max(dp[i-2]+h[i],dp[i-1]+l[i])
    return dp[n-1]
t=int(input())
for _ in range(t):
    n=int(input())
    h=list(map(int,input().split()))
    l=list(map(int,input().split()))
    print(fun(h,l,n))
