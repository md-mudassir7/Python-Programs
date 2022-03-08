
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    res={}
    for i in range(1,n+1):
        res[i]=0
    d={}
    for i in range(n-1):
        u,v=map(int,input().split())
        if u==1 or v==1:
            res[u]=x
        if u in d:
            d[u].append(v)
        else:
            d[u]=[v]
    for i in d:
        temp=res[i]
        for j in range(len(d[i])):
            res[d[i][j]]=temp*(j+1)
    ans=0
    for i in res:
        ans+=res[i]
    print(ans)
