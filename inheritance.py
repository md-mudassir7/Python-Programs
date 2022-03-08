class parent:
    parentattr=100
    def __init__(self):
        print('calling parent constructor !!')
    def parentmethod(self):               #method is same as function in c++
        print('Calling parent Method !! ')
    def setAttr(self,at):
        parent.parentattr=at
    def getAttr(self):
        print('parents attribute : ',parent.parentattr)

class child(parent):
    def __init__(self):
        print('calling child constructor !!')
    def childmethod(self):              
        print('Calling child Method !! ')


c=child()
c.childmethod()
p=parent()
c.setAttr(20)
p.getAttr()
