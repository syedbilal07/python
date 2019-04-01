# Overriding Methods

# You can always override your parent class methods. One reason for overriding parent's
#  methods is because you may want special or different functionality in your subclass.

class Parent:
    def myMethod(self):
        print("Calling Parent Method")


class Child(Parent):
    def myMethod(self):
        print("Calling Child Method")

c = Child()          # instance of child
c.myMethod()         # child calls overridden method