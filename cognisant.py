


n=int(input())
s=bin(n)[2:]
a=s.count('1')
b=s[::-1].index('1')
c=len(s)-1-s.index('1')
print(str(a)+"#"+str(b)+"#"+str(c))
