def fun(s):
    for i in range(len(s)):
        if s.count(s[i])>3:
            return False
        if (i+1)%4!=0:
            if not s[i].isalnum():
                return False
        else:
            if s[i]!="_":
                return False
    return True

s=input()
if fun(s):
    print('valid')
else:
    print('wrong_code')
        
    
    
