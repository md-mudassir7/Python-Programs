a,b,c=map(int,input().split())

if c%2==0:
    if a==-1*b or -1*a==b or a==b:
        print("=")
    elif a<0 and b<0:
        if a<b:
            print(">")
        else:
            print("<")
    elif a<0 and b>0:
        if -1*a>b:
            print(">")
        else:
            print("<")
    elif a>0 and b<0:
        if a>-1*b:
            print(">")
        else:
            print("<")
    elif a<0 and b==0:
        print(">")
    elif b<0 and a==0:
        print("<")
    elif a<b:
        print("<")
    else:
        print(">")
else:
    if a==b:
        print("=")
    elif a<b:
        print("<")
    else:
        print(">")
