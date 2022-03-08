import re

vowels=re.compile(r'[aeiouAEIOU]')
string='Today i am good'
match=vowels.findall(string)
print(match)
