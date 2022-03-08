
def check_set_bit(mask,j):
    i=1
    while j:
        i>>=1
        j-=1
    return (mask&i)==1

def count_set_bits(mask):
    temp=mask
    sum=0
    while temp:
        if (temp&1)==1:
            sum+=1
        temp=temp>>1
    return sum
def assign(n,mat):
    dp=[]
    for i in range(pow(2,n)):
        dp.append(2147483647)
    dp[0]=0
    for mask in range(pow(2,n)):
        t=bin(mask)[2:]
        t = "0"*(n-len(t))+t
        x=count_set_bits(mask)
        for j in range(n):
            if check_set_bit(mask,j):
                dp[mask|(1<<j)]=min(dp[mask|(1<<j)],dp[mask]+mat[x][j])
    print(*dp)
    print(dp[(2**n)-1])
n=int(input())
mat=[]
for _ in range(n):
    mat.append(list(map(int,input().split())))
assign(n,mat)
