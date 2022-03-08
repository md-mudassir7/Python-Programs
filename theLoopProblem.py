n=int(input())
for _ in range(n):
    a,b,c,d=map(int,input().split())
    t=0
    for i in range(c,d+1):
        t+=i
    res=0
    for i in range(a,b+1):
        res+=(t^i)
    print(res)
