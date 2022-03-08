

    l=list(map(int,input().split()))
    res={}
    for i in range(len(l)):
        if l[i] in res:
            res[l[i]]+=1
        else:
            res[l[i]]=1
    cnt=0
    for k,v in res.items():
        cnt+=v-1
    print(cnt)

