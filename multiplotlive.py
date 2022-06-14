import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, axs = plt.subplots(3,3)

def gL(index, rows, columns): #function to index times and temps to grid
    row = int(index/columns)
    columns = index%columns
    return [row,columns]  

times = [[] for i in range(7)]
temps = [[] for i in range(7)]

def animate(k):

    for i in range(7):

        times[i].append(np.genfromtxt("test.dat", usecols = i)[-1])
        temps[i].append(np.genfromtxt("test.dat", usecols = (i+7))[-1])

    for i in range(7):
        axs[gL(i,3,3)[0],gL(i,3,3)[1]].clear()
        axs[gL(i,3,3)[0],gL(i,3,3)[1]].plot(times[i],temps[i])



ani = animation.FuncAnimation(fig, animate, interval = 1500)


plt.show()
