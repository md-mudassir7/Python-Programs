print('1.Addition')
print('2.Substraction')
print('3.Multiplication')
print('4.Division')
print('5.Exit')


def add(a,b):
    print('The result of addition is : '+ str(a+b))

def sub(a,b):
    print('The result of substraction is : '+str(a-b))

def mul(a,b):
    print('The result of multiplication is : '+str(a*b))

def div(a,b):
    print('The result of ddivision is : '+str(a/b))
while True:
    choice=int(input('Enter choice : '))
    if (choice>=1 and choice<=4):
        print('Enter 2 numbers')
        num1=int(input('Enter 1st number : '))
        num2=int(input('Enter 2nd number : '))
        if choice==1:
            add(num1,num2)
        if choice==2:
            sub(num1,num2)
        if choice==3:
            mul(num1,num2)
        if choice==4:
            div(num1,num2)
    elif choice==5:
        break
    else:
        print('You have entered the wrong choice :')
