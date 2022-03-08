# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    b=list(map(int,input().split()))
    maxx=10**9
    res=[None]*n
    res[0]=0
    for i in range(1,n):
        if l[i]!=0:
            res[i]=0
        else:
            res[i]=maxx
    temp=-1


    for i in range(n):
        if l[i]==1:
            temp=i
        if temp!=-1:
            if l[i]==0:
                res[i]=min(res[i],i-temp)
    temp=-1
    for i in range(n-1,-1,-1):
        if l[i]==2:
            temp=i
        if temp!=-1:
            if l[i]==0:
                res[i]=min(res[i],temp-i)
    ans=[]
    for i in range(m):
        temp=b[i]-1
        if res[temp]!=maxx:
            ans.append(res[temp])
        else:
            ans.append(-1)
    print(*ans)
