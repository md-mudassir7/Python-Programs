
def lcs(x,y):
    m=len(x)
    n=len(y)
    L = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                continue
            elif x[i-1]==y[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    return L[m][n]

s=input()
s1=s[::-1]
print('Mininum Characters to be added to make ' +s+ ' a palindrome are  ' + str(len(s)-lcs(s,s1)))
