def rec(mat,s,p,n,t):
    for i in range(n):
        if mat[i][p]>t:
            s.add(i)
            rec(mat,s,i,n,mat[i][p])
def covid(l):
    mat=[]
    for i in range(len(l)):
        temp=[]
        for j in range(len(l)):
            if l[i]==l[j]:
                temp.append(-1)
            else:
                t=(i-j)/(l[j]-l[i])
                if t<=0:
                    temp.append(-1)
                else:
                    temp.append(t)
        mat.append(temp)
    s=set()
    v=[]
    for i in range(len(l)):
        s.add(i)
        rec(mat,s,i,len(l),0)
        v.append(len(s))
        s.clear()
    print(min(v),max(v))
                
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    covid(l)
