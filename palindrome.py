#code
def f(s):
	if len(s)%2==0:
		s1=s[:(len(s)//2)]
		s2=s[(len(s)//2):]
		i=len(s1)-1
		j=0
		while True:
			if int(s2[j])>int(s1[i]):
				s1=str(int(s1)+1)
				break
			elif int(s2[j])<int(s1[i]):
				break
			i=i-1
			j=j+1
		res=s1+s1[::-1]
		print(*list(res))
	else:
		s1=s[:(len(s)//2)]
		s2=s[(len(s)//2)]
		s3=s[(len(s)//2)+1:]
		i=len(s1)-1
		j=0
		while True:
			if int(s3[j])>int(s1[i]):
				if int(s2)==9:
					s2='0'
					s1=str(int(s1)+1)
					s3=str(int(s3[0])+1)+s3[1:]
				else:
					s2=str(int(s2)+1)
				break
			elif int(s2[j])<int(s1[i]):
				break
			i=i-1
			j=j+1
		res=s1+s2+s1[::-1]
		print(*list(res))
		
x=int(input())
for _ in range(x):
    n=int(input())
    l=list(map(int,input().split()))
    s=''
    for i in range(len(l)):
        s=s+str(l[i])
    f(s)
