def conv(var):
	try:
		print(int(var))
	except ValueError as arg:
		print('The arguement is not an integer\n',arg)


conv('www')

print('This part of the code comes after the exception ')
