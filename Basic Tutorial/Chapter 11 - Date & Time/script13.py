# The method strftime() converts a tuple or struct_time representing a time as returned by
# gmtime() or localtime() to a string as specified by the format argument.

import time

t = (2015, 12, 31, 10, 39, 45, 1, 48, 0)
t = time.mktime(t)
print (time.strftime("%b %d %Y %H:%M:%S", time.localtime(t)))