
n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
res=[l[0][0]+l[0][1]]
for i in range(1,n):
    res.append(res[len(res)-1]-l[i][0]+l[i][1])
print(max(res))
