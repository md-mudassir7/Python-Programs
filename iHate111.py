


for _ in range(int(input())):
    n=int(input())
    temp=n%11
    n-=temp*111
    if n>=0:
        print("YES")
    else:
        print("NO")
