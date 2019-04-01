def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print("This Argument Does Not Contain Any Number", Argument)

# Call above function here.
temp_convert("xyz")