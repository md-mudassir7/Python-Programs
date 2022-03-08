

lookup=[[] for _ in range(50)]
l=list(map(int,input().split()))
n=len(l)
for i in range(n):
    lookup[i].append(i)
j=1
while (1<<j)<=n:
    i=0
    while (i+(1<<j)-1)<n:
        if l[lookup[i][j-1]]<l[lookup[i+(1<<(j-1))][j-1]]:
            lookup[i][j]=lookup[i][j-1]
        else:
            lookup[i][j]=lookup[i+(1<<(j-1))][j-1]
        i+=1
    j+=1
print(lookup)
