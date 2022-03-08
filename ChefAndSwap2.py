def f(x):
    return int(x*(x+1)/2)
def fun(n):
    l=[x for x in range(1,n+1)]
    s=f(n)
    res=0
    if s&1:
        res=0
    else:
        x=(1+4*s)**0.5
        x=x-1
        x=x/2
        if x==int(x):
            res=res+f(n-x-1)+f(x-1)
        res=res+n-int(x)
    print(int(res))

t=int(input())
for _ in range(t):
    n=int(input())
    fun(n)
