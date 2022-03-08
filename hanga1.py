

l=list(map(str,input().split()))
res=0
t=[]
for i in l:
    if i in t:
        t.remove(i)
        res-=1
    else:
        t.append(i)
        res+=1
    
print(t)
print(res)
