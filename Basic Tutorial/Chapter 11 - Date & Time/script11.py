# The method mktime() is the inverse function of localtime(). Its argument is the struct_time or full 9-tuple
# and it returns a floating point number, for compatibility with time()

import time

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime( t )
print "time.mktime(t) : %f" %  secs
print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))