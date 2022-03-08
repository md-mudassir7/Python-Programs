exam_marks={'Anna':'A','Aamma':'B','Akka':'C','Tangi':'E','Avva':'A','Appa':'F'}
person_name=input('Enter the name of the person  : ')

if person_name in exam_marks:
    print('The marks of ' + person_name + ' is ' + exam_marks[person_name])
else:
    print('Name does not exist in the dictionary ')
