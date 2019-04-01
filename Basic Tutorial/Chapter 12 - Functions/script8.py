# Variable-length arguments

# You may need to process a function for more arguments than you specified while defining the function.
#  These arguments are called variable-length arguments and are not named in the function definition,
# unlike required and default arguments.

# An asterisk (*) is placed before the variable name that holds the values of all nonkeyword
# variable arguments. This tuple remains empty if no additional arguments are specified during
# the function call.

# Function definition is here
def printinfo(arg1, *vartuple):
    "Definition goes here"
    print("Output Is :")
    print(arg1)
    for var in vartuple:
        print (var)
    return;

# Now you can call printinfo function
printinfo(10)
printinfo(20,30,40)