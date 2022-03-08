# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=[]
    for i in range(len(b)):
        if l[b[i]-1]==1 or l[b[i]-1]==2:
            res.append(0)
            continue
        if l[b[i]-1]==0:
            temp1=l[0:(b[i]-1)]
            temp2=l[(b[i]):n]
            t1 = 1 in temp1
            t2 = 2 in temp2
            if t1==True and t2==True:
                x=temp1.index(1)+1
                y=temp2.index(2)+b[i]+1
                z=b[i]
                res.append(min(abs(z-x),abs(y-z)))
                continue
            if t1==True and t2==False:
                x=temp1.index(1)+1
                res.append(abs(b[i]-x))
                continue
            if t1==False and t2==True:
                y=temp2.index(2)+1+b[i]
                z=b[i]
                res.append(abs(y-z))
                continue
            if t1==False and t2==False:
                res.append(-1)
                continue
    print(*res)
