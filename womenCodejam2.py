

s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for j in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    res='A'
    for i in range(n):
        if i%2==0:
            res+=s[1:(l[i]+1)]
        else:
            res+=s[1:(l[i]+1)][::-1]
    print("Case #"+str(j+1)+": "+str(res))
