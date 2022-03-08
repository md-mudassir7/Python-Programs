s=input()
words=list(map(str,input().split()))
strings=[]
for i in range(len(words)):
    for j in range(i+1,len(words)+1):
        strings.append(words[i:j])
print(strings)
