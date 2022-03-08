
def fun(a):
    if a.isalnum():
        for i in range(len(a)):
            if a[i]==a[i+1]:
                return 1
    return -1
a=input()
fun(a)
