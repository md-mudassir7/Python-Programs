import re

phonenumber=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #Our phone number pattern is 555-555-5555(example)
string='''My phone number is : 321-152-5555
My friend phone number is : 123-456-7891
and my brothers phone number is : 1234-567-890'''
match=phonenumber.search(string) #search extracts only the first matched string
match2=phonenumber.findall(string) #findall  extracts all the string matched to the regular-expression
print('1',match.group()) #group is used to extract the number from the string of the search output
print('2',match2)           #match2 is a list as it finds multiple searched objects

phonenumber2=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #dividing phone.no in 2 groups 555 and 555-5555 for example
match1=phonenumber2.search(string)
a,b=match1.groups()
print('3',a,b)
print('4',match1.group(1)) #for printing the first group of mathced string
print('5',match1.group(2)) #for printing the second group of mathced string
print('6',match1.group())  #for printing the entire group of mathced string

