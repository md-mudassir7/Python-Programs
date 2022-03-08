import re
#The sub module replaces the matched string with a replace string from the given string
#The subn module replaces the matched string with a replace string from the given string and returns a tuple 
# containing the output string and number of times it performed the replace process
pattern='\s+' #which is a pattern for spaces
string='hi hello welcome to my program on using sub  and subn function'
replace=''
res=re.sub(pattern,replace,string) #replaces all spaces with empty character
print(res)
res1=re.sub(pattern,replace,string,2)#replaces first 2 spaces with empty character
print(res1)
res3=re.subn(pattern,replace,string) #replaces and returns a tuple containing the output string and number of times it performed the replace process
print(res3)
