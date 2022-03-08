computers = {"google":"chromebook","apple":"macbook","microsoft":"surface pro"}
computers.setdefault("lenovo","thinkPad")
print(computers)
computers.setdefault("lenovo","ideapad") #Wont change as lenovo is already set by default
print(computers)
computers.setdefault("apple","macbook pro")  #Wont change as apple is already in dict
print(computers)