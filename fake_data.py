import time
import numpy as np

k = 0

f = open("test.dat", "a")

while(True):
    time.sleep(0.5)
    data = np.random.rand(7,1)
    f.write(str(k)+"\t"  + str(k)+"\t"+ str(k)+"\t"+ str(k)+"\t"+ str(k)+"\t"+ str(k)+"\t"+str(k)+"\t"+str(data[0][0])+"\t"+str(data[1][0])+"\t"+str(data[2][0])+"\t"+str(data[3][0])+"\t"+str(data[4][0])+"\t"+str(data[5][0])+"\t"+str(data[6][0])+"\n")
    k += 1
    f.flush()
