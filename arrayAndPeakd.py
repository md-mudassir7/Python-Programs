t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if n%2==0:
        t=n//2-1
    else:
        t=n//2
    if k>t:
        print(-1)
        continue
    else:
        if k==0:
            l=[x for x in range(1,n+1)]
            print(l)
            continue
        t=1
        l=[1,3,2]
        for i in range(3,n,2):
            if t>=k:
                break
            else:
                l.append(l[i-1]+3)
                l.append(l[i-1]+2)
                t+=1
        t1=max(l)
        for i in range(t1+1,n+1):
            l.append(i)
        print(l)
