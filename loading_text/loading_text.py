import sys
import time
def load_data(): # this function is for funny lines...
    for i in range(101):
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
        sys.stdout.flush()
        time.sleep(0.01)
    print("")

load_data()