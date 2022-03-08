

t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    res,cnt=0,1
    k=0
    for i in range(len(l)):
        if k>=n:
            break
        res+=l.count(l[k])*cnt
        k+=l.count(l[k])
        cnt+=1
    print("Case #"+str(j+1)+": "+str(res))
