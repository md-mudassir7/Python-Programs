class vector:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def __str__(self):
		return 'vector (%d,%d) ' %(self.a,self.b)
	def __add__(self,other):
		return vector(self.a+other.a,self.b+other.b)

v1=vector(5,10)
v2=vector(2,5)
str(v1)    #string method of above class
str(v2)
print(v1+v2)  #__add__ method of above class
