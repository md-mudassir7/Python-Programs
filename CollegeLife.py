import sys
sys.setrecursionlimit(1500000)
def fun(n,e,h,a,b,c):
    ans=float('inf')
    if n<=0:
        return 0
    if n<=e and n<=h:
        ans=min(ans,n*c)
    if 2*n<=e:
        ans=min(ans,n*a)
    if 3*n<=h:
        ans=min(ans,n*b)
    if (h-n)//2>=1 and (h-n)//2>=(n-e):
        if (b-c)<0:
            x=min(n-1,(h-n)//2)
            ans=min(ans,((b-c)*x+n*c))
        else:
            x=max(1,n-e)
            ans=min(ans,((b-c)*x+n*c))
    if (e-n)>=1 and (e-n)>=(n-h):
        if (a-c)<0:
            x=min(n-1,e-n)
            ans=min(ans,((a-c)*x+n*c))
        else:
            x=max(1,n-h)
            ans=min(ans,((a-c)*x+n*c))
    if e//2>=1 and e//2>=((3*n-h+2)//3):
        if (a-b)<0:
            x=min(n-1,e//2)
            ans=min(ans,((a-b)*x+n*b))
        else:
            x=max(1,(3*n-h+2)//3)
            ans=min(ans,((a-b)*x+n*b))
    if (e>=3 and h>=4 and n>=3):
        ans=min(ans,(a+b+c+fun(n-3,e-3,h-4,a,b,c)))
    return ans
def fun1(n,e,h,a,b,c):
    y=fun(n,e,h,a,b,c)
    if y==float('inf'):
        print(-1)
    else:
        print(y)
t=int(input())
for _ in range(t):
    n,e,h,a,b,c=map(int,input().split())
    fun1(n,e,h,a,b,c)
                    
