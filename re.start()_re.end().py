import re
s=input()
k=input()

for i in range(len(s)):
    m=re.search(r'k',s)
    print('('+m.start()+','+m.end()+')')
    

