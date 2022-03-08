

import math
t=int(input())
for _ in range(t):
    n=int(input())
    if n<10:
        print(n)
    elif math.log10(n)==int(math.log10(n)):
        print(9*(str(n).count('0')))
    elif str(n)[:2]=='10':
        res='9'*(len(str(n))-1)
        res=int(res)
        ans=9*(len(str(res))-1)+res//int('1'*len(str(res)))
        print(ans)
    else:
        res=str(n)[0]+str(n)[0]*(len(str(n))-1)
        res=int(res)
        if n<int(res):
            res=res-int('1'*len(str(res)))
        ans=9*(len(str(res))-1)+res//int('1'*len(str(res)))
        print(ans)
        
