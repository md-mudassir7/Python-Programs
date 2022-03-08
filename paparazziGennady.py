def fun(l,n):
    if n==2:
        print(1)
    else:
        ans=1
        a=[]
        for i in range(len(l)):
            a.append([i,l[i]])
        a1=[]
        a1.append(a[0])
        a1.append(a[1])
        l=len(a1)
        for i in range(2,n):
            while len(a1)>=2:
                slope1=(a1[l-1][1]-a1[l-2][1])/(a1[l-1][0]-a1[l-2][0])
                slope2=(a[i][1]-a1[l-1][1])/(a[i][0]-a1[l-1][0])
                if slope1<=slope2:
                    a1.pop()
                    l-=1
                else:
                    break
            a1.append(a[i])
            l+=1
            ans=max(ans,a1[l-1][0]-a1[l-2][0])
        print(ans)
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    fun(l,n)
