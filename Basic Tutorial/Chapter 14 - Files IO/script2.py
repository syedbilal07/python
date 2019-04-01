# Open a file
fo = open("myfile.txt", "wb")
print("Name of file:", fo.name)
print("Closed or not:", fo.closed)
print("Opening mode:", fo.mode)
fo.close()