def fun(n,p):
    s=0
    e=n
    while s<=e:
        mid=(s+e)/2
        if mid**2==n:
            ans=mid
            break
        elif mid**2<n:
            s=mid+1
            ans=mid
        else:
            e=mid-1
    inc=0.1




    for i in range(p):
        while ans**2<=n:
            ans+=inc
        ans-=inc
        inc/=10
    print(ans)
n,p=map(int,input().split())
fun(n,p)
