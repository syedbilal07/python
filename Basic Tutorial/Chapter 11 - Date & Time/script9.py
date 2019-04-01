# The method gmtime() converts a time expressed in seconds since the epoch to a struct_time in UTC in which the dst flag
# is always zero.

import time

print "time.gmtime() : %s" % time.gmtime()

