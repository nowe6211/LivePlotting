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

ax_Button = plt.axes([.1, 0.05, 0.8, 0.07])
rangeButton = Button(ax_Button, "pause")


def pausedPlot(event):
    fig2, axs2 = plt.subplots()
    
    if rangeBox.text == "":
        range2 = 1
    else:
        range2= float(rangeBox.text)

    i2=0
    j2=0
    if range2 < len(x):
        while j2 < range2:
            i2 = i2+1
            j2 = x[-1] - x[-i2]  
    
    if i2 > len(x):
        axs2.plot(x,y)
    else:
        axs2.plot(x[-i2:],y[-i2:])
    plt.show()

rangeButton.on_clicked(pausedPlot)

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