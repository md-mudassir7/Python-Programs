n=int(input())
for _ in range(n):
    x=int(input())
    s=input()
    r=s[::-1]
    flag=0
    for i in range(len(r)):
        if s[i:] in s[:i]:
            print(s[i:],'YES')
            flag=1
            break
    if(flag==0):
        print('NO')
    
    
