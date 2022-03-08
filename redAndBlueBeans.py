
t=int(input())
for _ in range(t):
    r,b,d=map(int,input().split())
    if abs(r-b)<=d:
        print('YES')
    else:
        print('NO')
