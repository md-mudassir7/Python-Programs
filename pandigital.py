# Enter your code here. Read input from STDIN. Print output to STDOUT
def fun(n,k):
    s=str(n)
    temp=[str(x) for x in range(1,k+1)]
    s=s[:k]
    s=sorted(s)
    s=list(s)
    if s==temp:
        return True
    return False

a=int(input())
b=int(input())
k=int(input())
n=2
cnt=2
while True:
    t=str(n)
    t=t[::-1]
    t=int(t)
    if fun(n,k) and fun(t,k):
        print(n)
        print(cnt)
        break
    cnt+=1
    n=a+b
    a=b
    b=n
   
    if cnt>2*10**6:
        print("no solution")
        break
    
