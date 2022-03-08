
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    if s==n:
        print(0)
        continue
    if s<n:
        print(1)
        continue
    if s>n:
        print(s-n)
        continue
