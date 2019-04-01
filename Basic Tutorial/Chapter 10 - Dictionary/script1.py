dict = {'Name': 'Zara', 'Age': 25, 'Class': 'MCOM'}

print("Zara's Age Is", dict['Age'])
print("Zara Is A Student Of", dict['Class'])

dict['Age'] = 23; # update existing entry
dict['Class'] = "BCOM" # Add new entry

print("In 2015, Zara's Age Was", dict['Age'])
print("She Studied", dict['Class'])

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

#print ("dict['Age']: ", dict['Age'])
#print ("dict['School']: ", dict['Class'])