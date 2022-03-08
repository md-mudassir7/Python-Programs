
import sys
def assign(mat,n):
    dp=[]
    for _ in range(2**n):
        dp.append(sys.maxsize)
    dp[0]=0
    for mask in range(2**n):
        temp=bin(mask)[2:]
        temp='0'*(n-len(temp))+temp
        x=temp.count('1')
        for j in range(n):
            if temp[::-1][j]!='1':
                dp[mask|(1<<j)]=min(dp[mask|(1<<j)],dp[mask]+mat[x][j])
    print(*dp)
    return dp[2**n-1]

n=int(input())
mat=[]
for _ in range(n):
    mat.append(list(map(int,input().split())))
print(assign(mat,n))
