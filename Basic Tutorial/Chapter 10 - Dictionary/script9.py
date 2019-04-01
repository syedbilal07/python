# The method get() returns a value for the given key. If key is not available then returns default value None.

dict = {'Name': 'Zara', 'Age': 27}

print ("Value : %s" %  dict.get('Age'))
print ("Value : %s" %  dict.get('Sex', "NA"))