


def mergeIntervals(arr):
    m = []
    s = -10000
    max = -100000
    for i in range(len(arr)):
        a = arr[i]
        if a[0] > max:
            if i != 0:
                m.append([s,max])
            max = a[1]
            s = a[0]
        else:
            if a[1] >= max:
                max = a[1]
    if max != -100000 and [s, max] not in m:
        m.append([s, max])
    for i in range(len(m)):
        print(m[i], end = " ")
for _ in range(int(input())):
    n,k,f=map(int,input().split())
    l=[]
    for i in range(n):
        x,y=map(int,input().split())
        l.append([x,y])
    mergeIntervals(l)
