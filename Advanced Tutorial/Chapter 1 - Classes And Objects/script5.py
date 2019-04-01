# Overloading Operators

# Suppose you have created a Vector class to represent two-dimensional vectors,
# what happens when you use the plus operator to add them? Most likely Python will
# yell at you.

# You could, however, define the __add__ method in your class to perform vector
# addition and then the plus operator would behave as per expectation

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector: %d %d" % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, 2)
print (v1 + v2)