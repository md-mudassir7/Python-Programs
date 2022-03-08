t=int(input())
for _ in range(t):
    n=int(input())
    n=2*n-1
    res=0
    for i in range(1,n+1,2):
        if i==n:
            res+=i
        else:
            res+=2*i
    res1=6+2*3+(n-3)*4
    print(res,res1)
    
