
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if max(a)>min(b):
    print(0)
else:
    print(-max(a)+min(b)+1)
