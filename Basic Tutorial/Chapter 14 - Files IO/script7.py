# File Positions

# The tell() method tells you the current position within the file; in other words, the next read or write will
# occur at that many bytes from the beginning of the file.

## The seek(offset[, from]) method changes the current file position. The offset argument indicates the number
#  of bytes to be moved. The from argument specifies the reference position from where the bytes are to
#  be moved.

## If from is set to 0, it means use the beginning of the file as the reference position and 1 means use the
#  current position as the reference position and if it is set to 2 then the end of the file would be taken
# as the reference position.

fo = open("myfile.txt", "r+")
str = fo.read(25)
print("Read String Is", str)

# Check current position
position = fo.tell()
print("Current Position Is", position)

# Reposition pointer at the beginning once again
position = fo.seek(0,0)
str = fo.read(20)
print("Read String Is", str)
fo.close()