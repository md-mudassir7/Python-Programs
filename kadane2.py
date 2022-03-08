def kadane(A):
    maxSoFar = 0
    maxEndingHere = 0
    start = end = 0
    beg = 0
    for i in range(len(A)):
        maxEndingHere = maxEndingHere + A[i]
        if maxEndingHere < 0:
            maxEndingHere = 0        
            beg = i + 1
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
            start = beg
            end = i
    return maxSoFar,A[start: end + 1]

n=int(input())
s=input()
l=list(map(int,s.split()))
res,l2=kadane(l)
print(res)
s2=''
for i in range(len(l2)):
    if i==len(l2)-1:
        s2+=str(l2[i])
    else:
        s2+=str(l2[i])+" "
s=s.replace(s2,'')
l2=list(map(int,s.split()))
res2,l3=kadane(l2)
print(res2)
