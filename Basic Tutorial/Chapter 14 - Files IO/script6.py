# The read() Method

fo = open("myfile.txt", "r+")
str = fo.read(26) # Here, passed parameter is the number of bytes to be read from the opened file.
print("Read String Is", str)
fo.close()