class Employee:
    "Common Base Class For All Employees"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employee Are %d" % Employee.empCount)
    def displayEmployee(self):
        print("Name:", self.name, ", Salary:", self.salary)

#This would create first object of Employee class"
emp1 = Employee("Bilal", 25000)
#This would create second object of Employee class"
emp2 = Employee("Ammar", 3000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employees %d:" % Employee.empCount)

## You can add, remove, or modify attributes of classes and objects at any time −

emp1.salary = 4000  # Add an 'salary' attribute.
emp1.name = 'Huzaifa'  # Modify 'age' attribute.
del emp1.salary  # Delete 'age' attribute.

# Other Way Is To Use Built-in Methods

hasattr(emp1, 'salary')    # Returns true if 'salary' attribute exists
# getattr(emp1, 'salary')    # Returns value of 'salary' attribute
setattr(emp1, 'salary', 7000) # Set attribute 'salary' of 7000
delattr(emp1, 'salary')    # Delete attribute 'salary'

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )