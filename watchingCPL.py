t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    t1=[]
    sum=0
    l.sort()
    t1.append(l[n-1])
    sum=l[n-1]
    res=-1
    for i in range(n-2,-1,-1):
        t2=[]
        sum=sum+l[i]
        it=iter(t1)
        cnt=len(t1)
        while cnt>0:
            temp=next(it)
            t2.append(temp)
            t2.append(l[i])
            t2.append(temp+l[i])
            if (temp+l[i])>=k and (sum-temp-l[i])>=k:
                res=n-i
                break
            if l[i]>=k and (sum-l[i])>=k:
                res=n-i
                break
            cnt-=1
        if res!=-1:
            break
        t1=t2
    print(res)
