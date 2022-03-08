

res=''
while binary!=None:
    res+=str(binary.data)
    binary=binary.next
return int(res,2)
