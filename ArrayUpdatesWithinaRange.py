


def f(a,l,h):
    a[l]+=1
    if h!=(len(a)-1):
        a[h+1]-=1
    

  
x=int(input())
l=[0]*10
for _ in range(x):
    low,high=input().split()
    low=int(low)
    high=int(high)
    f(l,low,high)
for i in range(1, len(l)):
    l[i] += l[i - 1] 
print(*l)
