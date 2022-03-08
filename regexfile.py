import re
file=open('emails.txt','rt')
file_text=file.read()
emails=re.findall(r'[\w.-]+@[\w.-]+',file_text) #[\w.-] is used as matching pattern for a character
print(emails)
file.close()
