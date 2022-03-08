n,k=map(int,input().split())
l=list(map(int,input().split()))
t=max(l)
temp=[]
for i in range(1,t+1):
  if i not in l:
    temp.append(i)
for _ in range(k):
    i=int(input())
    if i<=len(temp):
        print( temp[i-1])
    else:
        if temp==[]:
            print(max(l)+i)
        else:
            print(temp[len(temp)-1]+i)
