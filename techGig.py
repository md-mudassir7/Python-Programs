gl=[]
def primes(a,b):
    while (a < b):
        flag = 0;
        for i in range(2, int(a/2),1):
            if(a % i == 0):
                flag = 1;
            break
        if (flag == 0):
            gl.append(a)
        a = a + 1
for _ in range(int(input())):
    l,r=map(int,input().split())
    primes(l,r)
    if len(gl)==0:
        print(-1)
    else:
        print(max(gl)-min(gl))
