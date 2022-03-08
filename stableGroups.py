



n,k,x=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
res=[]
for i in range(1,n):
    if l[i]-l[i-1]>x:
        res.append((l[i]-l[i-1])//x)

res.sort(reverse=True)



while(len(res)):
    if res[len(res)-1]<=k:
        k-=res[len(res)-1]
        res.pop(-1)

    else:
        break
print(len(res)+1)
