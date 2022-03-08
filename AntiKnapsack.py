
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    res=[x for x in range(1,n+1)]
    for i in range(1,n+1):
        if i==k or sum(res[:i])==k:
            res.remove(i)
    print(len(res))
    print(*res)
