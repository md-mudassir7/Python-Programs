t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    res=[0 for i in range(n)]
    for i in range(n):
        temp=l[i]
        for j in range(n):
            for k in range(j+1,n):
                if l[i] in l[j:k]:
                    temp=l[i]
                    for h in range(j,k+1):
                        temp = max(temp,temp&l[h])
        res[i]=temp
    print(*res)
