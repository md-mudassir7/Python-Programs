
def fun(t,d,s,n):
    t.sort()
    if s<t[0]:
        return "NO"
    else:
        cnt=0
        for i in range(len(t)):
            if s>t[i]:
                cnt+=1
                s+=d[t[i]]
        if cnt==n:
            return "YES"
        else:
            return "NO"
s,n=map(int,input().split())
d={}
t,t1=[],[]
for _ in range(n):
    x,y=map(int,input().split())
    t.append(x)
    t1.append(y)
    d[x]=y
print(fun(t,d,s,n))
