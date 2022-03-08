class employee:
    empcount=0
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        employee.empcount+=1
    def displaycount(self):
        print('Total employee number is ' + str(employee.empcount))
    def displayinfo(self):
        print('\nName: ',self.name,'Email: ',self.email,'Age: ',self.age)


e1=employee('Mohammed','Mohammed@gmail.com',20)
e2=employee('Mudassir','Mudassir@gmail.com',20)
e1.displaycount()
