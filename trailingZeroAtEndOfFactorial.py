def f(n):
    cnt=0
    while(n//5!=0):
        cnt=cnt+n//5
        n=n//5
    print(cnt)

x=int(input())
for _ in range(x):
    a=int(input())
    f(a)
