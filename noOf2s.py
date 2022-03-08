def f(n):
    cnt=1
    for i in range(2,n+1):
        if str(i).count('2')>0:
            cnt=cnt+1
    print(cnt)

x=int(input())
for _ in range(x):
    n=int(input())
    f(n)
