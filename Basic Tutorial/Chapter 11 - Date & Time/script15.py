# The method time() returns the time as a floating point number expressed in seconds since
# the epoch, in UTC

import time

print ("time.time(): %f " %  time.time())
print (time.localtime( time.time() ))
print (time.asctime( time.localtime(time.time()) ))