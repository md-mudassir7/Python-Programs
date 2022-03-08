import os

directory=input('Enter the directory : ')
os.chdir(directory)
print('The files in current directory are :')
print(os.listdir())
file_name=input('Enter the name of the file : ')
f1=open(file_name,'r')
for line in f1.readlines():
    f1=open(file_name,'r')
    line=line.strip('\n')
    f1.close()
    f1=open(file_name,'a')
    line='\n'+line
    f1.write(line[::-1])
    f1.close()
