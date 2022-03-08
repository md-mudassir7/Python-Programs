import re
#1.Using '|' to find the first occurance
regex=re.compile(r'Hello|World') #'|' is used to find the first match in a string
string='Hello World'
match=regex.search(string) #here the first match is hello from the string
print(match.group())
string2='World Hello'
match2=regex.search(string2) #here the first match is world from the string2
print(match2.group())


#2.Matching using ?,? is used to consider a substring of a string as an option when searching
string3= 'We are playing basball using basketball'
match3=re.findall(r'bas(ket)?ball',string3)
# here the sub-string ket is an optional string ,hence the
#compiler will consider ket as an option and outputs the matched string if it's there or not
print(match3)

#3.Using {} to match a repeated set of substring out of a string
string4='HelloHelloHello everyone'
regex2=re.compile(r'{Hello}{3}')
match4=regex2.findall(string4)
print(match4)

#4.Using '^' to match a pattern at start of a string
regex3=re.compile(r'^Hello')
match5=regex3.search('Hello World')
print(match5.group())
match6=regex3.search('World Hello')
#print(match6.group()) does'nt match as Hello is not at the start

#5 Using '$' to find a pattern that ends in the given string
regex4=re.compile(r'\d$')
match7=regex4.search('My roll number is 116')
print(match7.group())

#6 Using '.' to find all strings ending with some pattern given
regex5=re.compile(r'.ad')
match8=regex5.findall('Bad Sad glad mad had')
print(match8) #glad has 4 letters and only lad gets printed as .reprents only one character

#7 Using split function to remove sub-strings that match a pattern from a given string
regex6=re.compile(r'\d+')
match9=regex6.split('Twelve:12 Nine:9') #splits(removes) the patterns that matches a number (\d+)
print(match9)
