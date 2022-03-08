

n,q=map(int,input().split())
s=input()
d,d1=dict(),dict()
for i in range(n):
for _ in range(q):
    l,r=map(int,input().split())
    res=0
    d=dict()
    for i in range(l-1,r):
        if s[i] not in d:
            d[s[i]]=1
        else:
            d[s[i]]+=1


    for i in d:
        res+=(ord(i)-96)*d[i]
    print(res)
