
def fun(a,f):
    k={}
    for i in range(1,10):
        if str(i) in a and i<f[i-1]:
            d=f[i-1]
            k[ord(str(i))]=ord(str(d))
    print(k)
    a=a.translate(k)
    print(a)
a=input()
f=[]
for i in range(9):
    f.append(int(input()))
fun(a,f)
