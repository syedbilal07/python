# Class Inheritance

# Instead of starting from scratch, you can create a class by deriving it from a
#  preexisting class by listing the parent class in parentheses after the new class
#  name.

class Parent: # define parent class
    parentAttr = 100
    def __init__(self):
        print("Calling Parent Constructor")

    def parentMethod(self):
        print("Calling Parent Method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent Attribute:", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Calling Child Constructor")

    def childMethod(self):
        print("Calling Child Method")

c = Child() # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


