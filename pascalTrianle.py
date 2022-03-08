
def fun(n):
    arr = [[0 for x in range(n)] for y in range(n)]
    print(arr)
    for line in range(n):
        for i in range(0,line+1):
            if i==line or i==0:
                arr[line][i]=1
            else:
                arr[line][i]=arr[line-1][i-1]+arr[line-1][i]
            print(arr[line][i],end=" ")
        print()
        



n=int(input())
fun(n)
