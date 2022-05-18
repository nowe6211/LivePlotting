import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import TextBox, Slider, Button

# live animating with live data with ability to call a range of a recent data

range = 10
minutes = 0
hours = 0
seconds = 10
fig1, axs1 = plt.subplots()
plt.subplots_adjust(bottom=0.4)
x = []
y = []

plt.gcf().text(0.1, 0.20, "Select \nRange", fontsize = 10, weight = "bold")

ax_boxH = plt.axes([0.3, 0.19, 0.1, 0.07])
rangeBoxH = TextBox(ax_boxH, "Hours", initial = 0)

ax_boxM = plt.axes([0.55, 0.19, 0.1, 0.07])
rangeBoxM = TextBox(ax_boxM, "Minutes", initial = 0)

ax_boxS = plt.axes([0.8, 0.19, 0.1, 0.07])
rangeBoxS = TextBox(ax_boxS, "Seconds", initial = 10)



def animate(k):
    latest_time = np.genfromtxt("test_decay.dat", usecols = 0)[-1]
    latest_temp = np.genfromtxt("test_decay.dat", usecols = 1)[-1]
   
    
    x.append(latest_time)
    y.append(latest_temp)    
    
    axs1.clear()
    
    
    
    if rangeBoxH.text == "":
        hours = 0
    else:
        hours = float(rangeBoxH.text)
    
    if rangeBoxM.text == "":
        minutes = 0
    else:
        minutes = float(rangeBoxM.text)

    if rangeBoxS.text == "":
        minutes = 0
    else:
        seconds = float(rangeBoxS.text)

    range = seconds + 60*minutes + 3600*hours 
   
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
