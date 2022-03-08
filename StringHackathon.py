s=input()
d={}
temp=''
for i in range(len(s)):
    if s[i].isalpha():
        temp+=s[i]
    else:
        if temp!='':
           d[temp]=len(temp)
        temp=''
if s[len(s)-1].isalpha():
        d[temp]=len(temp)
key=max(d,key=d.get)
print(key,d[key])
