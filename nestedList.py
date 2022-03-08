def minimum(l):
    min=l[0][1]
    for i in range(len(l)):
        if l[i][1]<min:
            min=l[i][1]
    return min

l= [[input(), float(input())] for _ in range(int(input()))]
min1=minimum(l)
min2=99999
for i in range(len(l)):
    if l[i][1]!=min1 and l[i][1]<min2:
        min2=l[i][1]
l1=[]  
for i in range(len(l)):
    if l[i][1]==min2:
        l1.append(l[i][0])

l1=sorted(l1)
for i in range(len(l1)):
    print(l1[i])
        
