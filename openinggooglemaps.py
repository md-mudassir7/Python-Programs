import webbrowser,sys
#Go-to command prompt navigate to the directory where this file is present
#Type the name of this file(with .py extension) ,space and place you want to search
address=''.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place/'+address)
