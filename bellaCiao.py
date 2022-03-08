t=int(input())
for _ in range(t):
    D,d,P,Q=map(int,input().split())
    cnt=0
    res=0
    n=D//d
    for i in range(1,n+1,d):
        res+=(P+cnt*Q)
        cnt+=1
    n=D%d
    res+=n*(P+cnt*Q)
    print(res)
