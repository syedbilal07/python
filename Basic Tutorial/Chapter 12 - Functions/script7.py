# Default arguments
# A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.
#  The following example gives an idea on default arguments, it prints default age
# if it is not passed −

# Function definition is here
def printinfo( name, age = 26 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=24, name="Bilal" )
printinfo( name="Ahmer" )

