# Executing modules as scripts

# Within a module, the module???s name (as a string) is available as the value of the
#  global variable __name__. The code in the module will be executed, just as if you
# imported it, but with the __name__ set to "__main__". That means that by adding this
#  code at the end of your module

def fib(n):
    "Definition goes here"
    result = []
    a,b = 0,1
    while(b < n):
        result.append(b)
        a,b = b, a + b
    return result
# Calling module inside the module script

if __name__ == "__main__":
    f = fib(100)
    print(f)
