




for _ in range(int(input())):
    n,x,t=map(int,input().split())
    z=t//x
    if z>n:
        ans=n*(n-1)//2
        print(ans)
    else:
        ans=z*n
        ans-=z*(z+1)//2
        print(ans)
