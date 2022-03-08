t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    res,res1=[],[]
    for i in range(len(l)):
        if l[i]%2==0:
            res.append(l[i])
        else:
            res1.append(l[i])
    print(*(res1+res))
