# The method clock() returns the current processor time as a floating point number expressed in seconds on Unix.
# On Windows, this function returns wall-clock seconds elapsed since the first call to this function
# This method returns the current processor time as a floating point number expressed in seconds on Unix
# and in Windows it returns wall-clock seconds elapsed since the first call to this function, as a floating point number.

import time

def procedure():
    time.sleep(2.5)

# measure process time
to = time.clock()
procedure()
print time.clock(), "seconds process time"

# measure wall time
to = time.time()
procedure()
print time.time() - t0, "seconds wall time"
