

l=list(map(int,input().split()))
k=int(input())
t=sum(l)
if k==t:
    print(0)
if k>t:
    t1=k//t
    k-=t*t1
s=0
for i in range(len(l)):
    s+=l[i]
    if s>k:
        print(i)
        break
