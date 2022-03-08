from collections import defaultdict
def f(a,b):
    if len(a)==len(b):
        flag=0
        for i in range(len(a)):
            for j in range(i+1,len(a)+1):
                if a[i:j].count('1')%2==0 and a[i:j].count('1')>0:
                    if (a[0:i]+a[i:j][::-1]+a[j:len(a)])==b:
                            return True
    return False
t=int(input())
for _ in range(t):
    s=input()
    d=defaultdict(list)
    res=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j] not in d[len(s[i:j])]:
                d[len(s[i:j])].append(s[i:j])
    print(d)
    
