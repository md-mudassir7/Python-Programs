

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    s=input()
    s=list(s)
    for i in range(m):
        for j in range(n):
            if j==0:
                if s[1]=='1':
                    s[0]='1'
            if j==n-1:
                if s[j-2]=='1':
                    s[j-1]='1'
            elif s[j]=='0':
                if s[j-1]=='1' and s[j+1]=='1':
                    continue
                if s[j-1]=='1' and s[j+1]=='1':
                    s[j]=='1'
    print(''.join(s))
