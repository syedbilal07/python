# Data Hiding

# An object's attributes may or may not be visible outside the class definition.
# You need to name attributes with a double underscore prefix, and those attributes then
# are not be directly visible to outsiders.

class JustCounter:
    __secretCounter = 0

    def count(self):
        self.__secretCounter += 1
        print(self.__secretCounter)

counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secretCounter) # This will result in error
print(counter._JustCounter__secretCounter)