def isCubeSum(n):
     
    for i in range(1, int(pow(n, 1 / 3)) + 1):
        for j in range(1,int(pow(n, 1 / 3)) + 2):
            if (i * i * i + (j) *(j) * (j) == n):
                return True;
    return False;
 
for _ in range(int(input())):
    if isCubeSum(int(input())):
        print('YES')
    else:
        print('NO')
