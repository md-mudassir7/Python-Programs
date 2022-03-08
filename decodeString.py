# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    res=''
    for i in range(0,len(s),4):
	    temp=s[i:i+4]
	    temp=int(temp,2)
	    res+=chr(97+temp)
    print(res)
