# The method fromkeys() creates a new dictionary with keys from seq and values set to value.

seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print("New Dictionary %s " % str(dict))

dict = dict.fromkeys(seq, 10)
print("New Dictionary %s " % str(dict))