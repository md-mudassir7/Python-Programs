n=int(input())
l,t=[],[]
for i in range(n):
    l.append(int(input()))
    t.append(l[i])
t.sort()
s=t[0]+t[1]+t[-1]+t[-2]

for i in range(n-2,0,-1):
    t=l[:i+1]
    t.sort()
    r=t[0]+t[1]+t[-1]+t[-2]
    if r>s:
        k=n-i-1
        s=r
print(k)
