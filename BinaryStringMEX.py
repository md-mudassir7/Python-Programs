import itertools
def fun2(s1,s2):
    j=0
    for i in range(len(s2)):
        if s1[j]==s2[i]:
            j+=1
        if j==len(s1):
            return True
    return False
def fun(s):
    res=1
    while True:
        s1=bin(res)[2:]
        if fun2(s1,s)==False:
            return s1
        res+=1
        
for _ in range(int(input())):
    s=input()
    if '0' not in s:
        print(0)
    else:
        print(fun(s))

            
