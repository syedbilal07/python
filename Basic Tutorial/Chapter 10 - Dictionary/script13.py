# The method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.

dict = {'Name': 'Zara', 'Age': 7}

print ("Value : %s" %  dict.setdefault('Age', None))
print ("Value : %s" %  dict.setdefault('Sex', None))
print (dict)
