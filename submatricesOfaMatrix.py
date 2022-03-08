
n=int(input())
m=int(input())
l=[]
su=0
for i in range(n):
    l.append(list(map(int,input().split())))
    su+=sum(l[i])
print(su)
