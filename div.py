

n=int(input())
s=str(n)
s=s.replace('0','')
if s==s[::-1]:
    print('Yes')
else:
    print('No')
