# The method strptime() parses a string representing a time according to a format.
# The return value is a struct_time as returned by gmtime() or localtime().

import time

struct_time = time.strptime("30 12 2015", "%d %m %Y")
print ("tuple : ", struct_time)