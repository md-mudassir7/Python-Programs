
l=[]
def combinationUtil(arr, n, r,
                    index, data, i):
    # Current combination is
    # ready to be printed,
    # print it
    temp=[]
    if(index == r):
        for j in range(r):
            temp.append(data[j])
        l.append(temp)
        return
 
    # When no more elements
    # are there to put in data[]
    if(i >= n):
        return
 
    # current is included,
    # put next at next
    # location
    data[index] = arr[i]
    combinationUtil(arr, n, r,
                    index + 1, data, i + 1)
     
    # current is excluded,
    # replace it with
    # next (Note that i+1
    # is passed, but index
    # is not changed)
    combinationUtil(arr, n, r, index,
                    data, i + 1)
 
 
# The main function that
# prints all combinations
# of size r in arr[] of
# size n. This function
# mainly uses combinationUtil()
def printcombination(arr, n, r):
 
    # A temporary array to
    # store all combination
    # one by one
    data = list(range(r))
     
    # Print all combination
    # using temporary
    # array 'data[]'
    combinationUtil(arr, n, r,
                    0, data, 0)

for _ in range(int(input())):
    l=[]
    n,k=map(int,input().split())
    t=[i for i in range(1,n+1)]
    printcombination(t,n,k)
    res,index=0,0
    for i in range(len(l)):
        t=0
        for j in range(len(l[i])):
            t^=l[i][j]
        if t>res:
            res=t
            index=i
    print(*l[index])
