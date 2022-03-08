from collections import deque

def beauty(n,m,s,x,y):
    deg=[0 for i in range(n)]
    graph={i:[] for i in range(n)}
    c=0
    for i in range(m):
        x[i]-=1
        y[i]-=1
        graph[x[i]].append(y[i])
        deg[y[i]]+=1
    q=deque()
    for i in range(n):
        if deg[i]==0:
            q.append(i)
    l=[]
    for i in range(n):
        k=[]
        for j in range(26):
            k.append(0)
        l.append(k)
    while(c<n and q):
        a=q.popleft()
        c+=1
        l[a][ord(s[a])-97]+=1
        for i in graph[a]:
            for j in range(26):
                l[i][j]=max(l[i][j],l[a][j])
            deg[i]-=1
            if(deg[i]==0):
                q.append(i)
    if(c!=n):
        return -1
    else:
        result=0
        for i in range(n):
            result=max(result,max(l[i]))
        return result
n,m=map(int,input().split())
s=input()
x=[]
y=[]
for _ in range(m):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
print(beauty(n,m,s,x,y))
