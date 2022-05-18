import time
import numpy as np
import math

k = 0

f = open("test_decay.dat", "a")

while(True):
    time.sleep(0.5)
    data = np.random.rand()
    val = pow(math.e + data, -k )
    f.write(str(k)+"\t"+str(val)+"\n")
    k += 1
    f.flush()