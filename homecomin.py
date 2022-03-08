

a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    cnt=0
    for j in range(len(a)):
        if i!=j:
            if a[i]%a[j]==0 or a[j]%a[i]==0:
                cnt+=1
    l.append(cnt)
print(*l)
