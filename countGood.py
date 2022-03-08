

s=input()
cnt=0
j=0
for i in range(len(s)):
    if j+2>=len(s):
        break
    t=s[j:j+3]
    if len(list(t))==len(set(t)):
        cnt+=1
    j+=1
print(cnt)
