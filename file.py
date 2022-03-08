import os

directory=input('Enter the directory where you want to create the file (Use \\\ to separate directories) : ')

directory=directory.strip()

os.chdir(directory)

print('Currently we are in ' + os.getcwd()+' directory')

file_name=input('Enter the name of the file you want to create : ')

fn=open(file_name,'wt')

content='''Hi!!!!
Hello world
Welcome to my program
Fuck you!!!\n'''

fn.write(content)

fn.close()
