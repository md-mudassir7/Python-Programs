
import math
r,x,y=map(int,input().split())
t=math.sqrt(x**2+y**2)
if t==r:
    print(1)
elif t<=2*r:
    print(2)
else:
    print(math.ceil(t/r))
