t=int(input())
for _ in range(t):
    n,x,k=map(int,input().split())
    if x%k==0 or (n-x+1)%k==0:
        print("YES")
    else:
        print("NO")
        
