
import math
def fun(b,c):
    temp=(b**2)-4*c
    if temp>=0:
        temp2=(math.sqrt(temp))
        t1=(temp2-b)/2
        t2=(-temp2-b)/2
        if t1==int(t1) and t2==int(t2):
            return True
    return False
for _ in range(int(input())):
    l,r=map(int,input().split())
    res=0
    for i in range(l,r+1):
        for j in range(l,r+1):
            if fun(2*i,j):
                res+=1
    print(res)
