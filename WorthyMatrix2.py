
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    matrix=[]
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    #row-wise sum
    for i in range(n):
        for j in range(1,m):
            matrix[i][j]+=matrix[i][j-1]
    #column-wise sum
    for i in range(m):
        for j in range(1,n):
            matrix[j][i]+=matrix[j-1][i]
    #adding a row and a column of 0's to the matrix
    for i in range(n):
        matrix[i].insert(0,0)
    matrix.insert(0,[0 for _ in range(len(matrix[0]))])
    count=0
    order=1
    while order<n+1:
        i=order
        j=m
        for i in range(order,n+1):
            a=i-order+1
            b=j-order+1
            z=matrix[i][j]-matrix[a-1][j]-matrix[i][b-1]+matrix[a-1][b-1]
            if z/(order*order)<k:      
                i+=1
            else:
                start=order
                end=m
                while start<=end:
                    mid=(start+end)//2
                    a=i-order+1
                    b=mid-order+1
                    z=matrix[i][mid]-matrix[a-1][mid]-matrix[i][b-1]+matrix[a-1][b-1]
                    if z/(order*order)<k:
                        start=mid+1
                    else:
                        res=mid
                        end=mid-1
                count+=m-res+1
        order+=1
    print(count)
