

Max=int(4e6+5)
dp1=[i for i in range(Max)]
dp2=[0 for i in range(Max)]
for i in range(2,Max):
    if dp1[i]==i:
        dp1[i]=i-1
        j=2*i
        while j<Max:
            dp1[j]=(dp1[j]//i)*(i-1)
            j+=i
for i in range(1,Max):
    dp2[i]+=i-1
    j=2*i
    while j<Max:
        dp2[j]+=i*((1+dp1[j//i])//2)
        j+=i
for _ in range(int(input())):
    n=int(input())
    print(dp2[4*n+1])
