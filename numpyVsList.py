#aray in python takes mores size than numpy array
import sys
import numpy as np
import time

S=range(1000)
print(sys.getsizeof(5)*len(S))

D=np.arange(1000)
print(D.size*D.itemsize)
