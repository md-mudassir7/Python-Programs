


N=int(3e5+5)
n,m=map(int,input().split())
dp=[[0 for i in range(30)] for i in range(N+1)]
visited=[0 for i in range(N+1)]
ans=0
cycle=[0 for i in range(N+1)]
def dfs(src):
    global ans
    visited[src]=1
    cycle[src]=1
    for i in adj[src]:
        if cycle[i]==1:
            print(-1)
            exit()
        if visited[i]==0:
            dfs(i)
        for j in range(26):
            dp[src][j]=max(dp[src][j],dp[i][j])
    dp[src][ord(s[src-1])-97]+=1
    for i in range(26):
        ans=max(ans,dp[src][i])
    cycle[src]=0
adj=dict()
for i in range(1,n+1):
    adj[i]=[]
s=input()
for i in range(1,m+1):
    u,v=map(int,input().split())
    adj[u].append(v)
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
print(ans)
