def fun(mat,n,m,k,order):
    cnt=0
    while order<n+1:
        i=order
        j=m
        while i<n+1:
            x=i-order+1
            y=j-order+1
            z=mat[i][j]-mat[x-1][j]-mat[i][y-1]+mat[x-1][y-1]
            if z/(order**2)<k:      
                i+=1
            else:
                start=order
                end=m
                while start<=end:
                    mid=(start+end)//2
                    x=i-order+1
                    y=mid-order+1
                    z=mat[i][mid]-mat[x-1][mid]-mat[i][y-1]+mat[x-1][y-1]
                    if z/(order**2)<k:
                        start=mid+1
                    else:
                        ans=mid
                        end=mid-1
                cnt+=m-ans+1
                i+=1
        order+=1
    return cnt

t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    mat=[]
    for _ in range(n):
        mat.append(list(map(int,input().split())))
    for i in range(n):
        s=0
        for j in range(m):
            s+=mat[i][j]
            mat[i][j]=s
    for i in range(m):
        s=0
        for j in range(n):
            s+=mat[j][i]
            mat[j][i]=s
    for i in range(n):
        mat[i].insert(0,0)
    t=len(mat[0])
    l=[0 for _ in range(t)]
    mat.insert(0,l)
    print(fun(mat,n,m,k,1))
