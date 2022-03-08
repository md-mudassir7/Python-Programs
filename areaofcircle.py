print('Enter x to close the program')

def calc_area(rad):
    rad=float(rad)
    area=22/7*rad*rad
    print('The area of circle is ' + str(area))


while True:
    rad=input('Enter the radius of the circle : ')
    if rad=='x':
        break
    calc_area(rad)
