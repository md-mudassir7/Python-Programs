

t=int(input())
for _ in range(t):
    n=int(input())
    res=0
    while n>1:
        if n%2==0:
            res+=n//2
            n//=2
        else:
            res+=n//2+1
            n//=2

    print(res)
