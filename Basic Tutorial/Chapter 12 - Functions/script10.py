# The return Statement

# The statement return [expression] exits a function, optionally passing back an
# expression to the caller. A return statement with no arguments is the same as
#  return None.

# Function definition is here
def sum(arg1, arg2):
    "This is a function"
    # Add both the parameters and return them"
    total = arg1 + arg2
    print("Inside the function", total)
    return total

# Now you can call sum function
total = sum(10,20)
print("Outside the function", total)