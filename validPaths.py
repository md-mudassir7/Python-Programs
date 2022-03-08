
v,dp,dp1=[[]],[],[]
def dfs(cur,par):
    dp[cur],dp1[cur]=1,1
    s=0
    cnt=0
    for i in range(len(v[cur])):
        node=v[cur][i]
        if node!=par:
            dfs(node,cur)
            dp[cur]+=2*dp[node]
            dp[cur]%=1000000007
            cnt+=1
            dp1[cur]+=dp1[node]%(1000000007)
            dp1[cur]+=dp[node]%(1000000007)
            s+=dp[node]
    for i in range(len(v[cur])):
        node=v[cur][i]
        if node!=par:
            dp1[cur]+=(dp[node]*((s-dp[node])+1000000007)%1000000007)%1000000007
            dp1[cur]%=1000000007

for _ in range(int(input())):
    n=int(input())
    v.clear()
    dp.clear()
    dp1.clear()
    v,dp,dp1=[[None for _ in range(n+1)]for _ in range(n+1) ],[None for _ in range(n+1)],[None for _ in range(n+1)]
    for i in range(n-1):
        l,r=map(int,input().split())
        if l in v:
            v[l].append(r)
        else:
            v[l]=[r]
        if r in v:
            v[r].append(l)
        else:
            v[r]=[l]
    dfs(1,1)
    ans=dp1[1]%1000000007
    print(ans)
    
