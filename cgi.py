def printMagicNumbers(N,A,B):
    l=[A,B]
    for i in range(2,N):
        l.append(l[-1]+l[-2])
    for i in range(N):
        if l[i]%2==0:
            print(l[i],end=" ")
    print()
    for i in range(N):
        if l[i]%2>0:
            print(l[i],end=" ")
