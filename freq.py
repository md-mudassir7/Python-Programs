
for _ in range(int(input())):
    s=input()
    d={}
    res=0
    ans=s[0]
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]]=1
        else:
            d[s[i]]+=1
        if d[s[i]]==res:
            if ord(s[i])<ord(ans):
                ans=s[i]


        elif d[s[i]]>res:
            res=d[s[i]]
            ans=s[i]
    print(ans)
