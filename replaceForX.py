def fun(ar,x,p,k):
    ar.sort()
    cnt=0
    for i in range(len(ar)):
        print(*ar)
        if ar[p-1]==x:
            break
        elif (k>=p and ar[p-1]>=x):
            ar[p-1]=x
            cnt+=1
        elif (k<=p and ar[p-1]<=x):
            ar[p-1]=x
            cnt+=1
        else:
            cnt-=1
            break
        ar.sort()
    print(cnt)
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    p=l[2]
    k=l[3]
    ar=list(map(int,input().split()))
    fun(ar,x,p,k)
