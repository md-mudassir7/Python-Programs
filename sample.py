


cnt=0
def fun(l,i,j,n):
    if i==j:
        return 0
    if l[i]==l[j]:
        return fun(l,i+1,j-1,n)
    else:
        for k in range(n):
            if l[k]==l[j]:
                l[k]=l[i]
        global cnt
        cnt=cnt+1+min(fun(l,i,j,n),fun(l,j,i,n))
    return cnt
n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(0)
else:
    fun(l,0,n-1,n)
            
