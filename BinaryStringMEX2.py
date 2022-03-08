ma=int(1e6)
num0=[None for _ in range(ma)]
num1=[None for _ in range(ma)]
dp0=[None for _ in range(ma)]
dp1=[None for _ in range(ma)]
def fun():
    s=input()
    n=len(s)
    pos=-1
    for i in range(n):
        if s[i]=='0':
            for j in range(pos+1,i+1):
                num0[j]=i
            pos=i
    for i in range(pos+1,n):
        num0[i]=n
    if num0[0]==n:
        print('0')
        return
    pos=-1
    for i in range(n):  
        if s[i]=='1':
            for j in range(pos+1,i+1):
                num1[j]=i
            pos=i
    for i in range(pos+1,n):
        num1[i]=n
    dp0[n]=dp0[n+1]=dp1[n]=dp1[n+1]=0
    for i in range(n-1,-1,-1):
        dp0[i]=dp0[i+1]
        if s[i]=='0' and num1[i]<n:
            dp0[i]=max(dp0[i],dp0[num1[i]+1]+1)
        if s[i]=='1' and num0[i]<n:
            dp0[i]=max(dp0[i],dp0[num0[i]+1]+1)
        dp1[i]=dp1[i+1]
        if num1[i]<n:
            dp1[i]=max(dp1[i],dp0[num1[i]+1]+1)
    x=dp1[0]+1
    cnt=num1[0]+1
    ans='1'
    for i in range(1,x):
        if cnt>=n:
            ans+='0'
            continue
        if num0[cnt]>=n:
            ans+='0'
            cnt=num0[cnt]+1
            continue
        if dp0[num0[cnt]+1]<x-i-1:
            ans+='0'
            cnt=num0[cnt]+1
        else:
            ans+='1'
            cnt=num1[cnt]+1
    print(ans)
for _ in range(int(input())):
    fun()
