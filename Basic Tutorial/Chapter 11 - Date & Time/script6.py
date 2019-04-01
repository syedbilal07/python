# The method asctime() converts a tuple or struct_time representing a time as returned by gmtime() or localtime()
#  to a 24-character string of the following form: 'Tue Feb 17 23:21:05 2009'.

import time

t = time.localtime()
print "time.asctime(t): %s " % time.asctime(t)