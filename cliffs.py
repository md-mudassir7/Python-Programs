

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    res=[]
    start=l[1]-l[0]
    end=l[n-1]-l[n-2]
    dif=min(start,end)
    temp=-1
    for i in range(1,n-1):
        if l[i+1]-l[i]<dif:
            dif=l[i+1]-l[i]
            temp=i

    if temp==-1:
        if start<end:
            res.append(l[0])
            for i in range(2,n):
                res.append(l[i])
            res.append(l[1])
        else:
            res.append(l[n-2])
            for i in range(0,n):
                if i!=n-2:
                    res.append(l[i])
    else:
        res.append(l[temp])
        for i in range(temp+2,n):
            res.append(l[i])
        for i in range(temp):
            res.append(l[i])
        res.append(l[temp+1])
    print(*res)
