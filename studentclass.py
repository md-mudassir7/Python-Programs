class student:
    stucount=0
    def __init__(self,name,subject,marks):
        self.name=name
        self.subject=subject
        self.marks=marks
        student.stucount+=1
    def displaycount(self):
        print('The total number of students are : '+str(student.stucount))
    def displayinfo(self):
        print('Name : '+self.name+'\n'+'Subject : '+self.subject+'\n'+'Marks : '+self.marks)

print('Usage\n1-Add students\n2-Display students information\n3-Quit program')

while True:
    option=int(input('Enter your option : '))
    if option==1:
        name=input('Enter the name of the student : ')
        subject=input('Enter the subject : ')
        marks=input('Enter the marks : ')
        stud[student.stucount]=student(name,subject,marks)
    elif option==2:
        for i in range(0,student.stucount):
            stud[i].displayinfo()
    elif option==3:
        break
