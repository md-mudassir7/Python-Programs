
def fun(s):
    j=0
    t='hello'
    for i in s:
        if i==s[j]:
            j+=1
        if j==5:
            return "YES"
    return "NO"

s=input()
print(fun(s))
