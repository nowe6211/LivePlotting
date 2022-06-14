import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, axs = plt.subplots(3,3)


times = [[] for i in range(7)]
temps = [[] for i in range(7)]

def animate(k):

    for i in range(7):

        times[i].append(np.genfromtxt("test.dat", usecols = i)[-1])
        temps[i].append(np.genfromtxt("test.dat", usecols = (i+7))[-1])

    k = 0
    for i in range(3):
        for j in range (3):
            if k > 6:
                break
            else:
                axs[i,j].clear()
                axs[i,j].plot(times[k],temps[k])
                k = k +1


ani = animation.FuncAnimation(fig, animate, interval = 1500)


plt.show()