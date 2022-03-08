n=int(input())
l=list(map(int,input().split()))
low,high=0,n-1
res=0
while low<=high:
    if l[low]==l[high]:
        low+=1
        high-=1
    elif l[low]>l[high]:
        high-=1
        l[high]+=l[high+1]
        res+=1
    else:
        low+=1
        l[low]+=l[low-1]
        res+=1
print(res)
