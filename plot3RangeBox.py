import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import TextBox, Slider, Button

# live animating with live data with ability to call a range of a recent data

range = 10

fig1, axs1 = plt.subplots()
plt.subplots_adjust(bottom=0.4)
x = []
y = []

ax_box = plt.axes([0.1, 0.19, 0.8, 0.07])
rangeBox = TextBox(ax_box, "range", initial = 10)

def animate(k):
    latest_time = np.genfromtxt("test_decay.dat", usecols = 0)[-1]
    latest_temp = np.genfromtxt("test_decay.dat", usecols = 1)[-1]
   
    
    x.append(latest_time)
    y.append(latest_temp)    
    
    axs1.clear()
    
    if rangeBox.text == "":
        range = 1
    else:
        range = float(rangeBox.text)


   
    i=0
    j=0
    if range < len(x):
        while j < range:
            i = i+1
            j = latest_time - x[-i]  
    
    if k<i:
        axs1.plot(x, y)
    else:
        axs1.plot(x[-i:], y[-i:])




ani = animation.FuncAnimation(fig1, animate, interval = 500)
plt.show()