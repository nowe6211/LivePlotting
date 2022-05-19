import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import TextBox, Slider, Button

# live animating with live data with ability to call a range of a recent data

#set initial range
range = 10 

#creates initial plot
fig1, axs1 = plt.subplots()
plt.subplots_adjust(bottom=0.4)

#x and y data to be filled
x = []
y = []

#creates range input box
plt.gcf().text(0.1, 0.20, "Select \nRange", fontsize = 10, weight = "bold")

ax_boxH = plt.axes([0.3, 0.19, 0.1, 0.07])
rangeBoxH = TextBox(ax_boxH, "Hours", initial = 0)

ax_boxM = plt.axes([0.55, 0.19, 0.1, 0.07])
rangeBoxM = TextBox(ax_boxM, "Minutes", initial = 0)

ax_boxS = plt.axes([0.8, 0.19, 0.1, 0.07])
rangeBoxS = TextBox(ax_boxS, "Seconds", initial = 10)

#creates the pause button
ax_Button = plt.axes([.1, 0.05, 0.8, 0.07])
rangeButton = Button(ax_Button, "pause")


#function to create the pasued captaure of the current graph
def pausedPlot(event):

    #creates paused plot
    fig2, axs2 = plt.subplots()
    plt.subplots_adjust(bottom=0.4)

    #allows widgets to remain operable after it is passed through the pause function
    global ax_boxHP
    global rangeBoxHP
    global ax_boxMP
    global rangeBoxMP
    global ax_boxSP
    global rangeBoxSP
    
    #creates range input for paused plot
    plt.gcf().text(0.1, 0.20, "Select \nRange", fontsize = 10, weight = "bold")

    ax_boxHP = plt.axes([0.3, 0.19, 0.1, 0.07])
    rangeBoxHP = TextBox(ax_boxHP, "Hours", initial = 0)

    ax_boxMP = plt.axes([0.55, 0.19, 0.1, 0.07])
    rangeBoxMP = TextBox(ax_boxMP, "Minutes", initial = 0)

    ax_boxSP = plt.axes([0.8, 0.19, 0.1, 0.07])
    rangeBoxSP = TextBox(ax_boxSP, "Seconds", initial = 10)
    #sets range based off user intput to textbox, ensure the graph doesnt crash when box is empty
    try: 
        float(rangeBoxHP.text)
    except:
        hoursP = 0
    else:
        hoursP = float(rangeBoxHP.text)

    try: 
        float(rangeBoxMP.text)
    except:
        minutesP = 0
    else:
        minutesP = float(rangeBoxMP.text)

    try: 
        float(rangeBoxSP.text)
    except:
        secondsP = 0
    else:
        secondsP = float(rangeBoxSP.text)  

    range2 = secondsP + 60*minutesP + 3600*hoursP


    #grabs just the data from when plot was paused
    pausedLen = len(x)
    xP = x[0:pausedLen]
    yP = y[0:pausedLen]
    
    #paused indexing varibales
    i2=0
    j2=0

    #function that finds how many data points you need to go back until you are at the correct time range
    if range2 < len(xP):
        while j2 < range2:
            i2 = i2+1
            j2 = xP[-1] - xP[-i2]  
    
    #if not enough data points to fill the time range, plots the entire plot 
    if i2 > len(xP):
        axs2.plot(xP,yP)
    else:
        axs2.plot(xP[-i2:],yP[-i2:])
  
#redraws plot with new range
    def update(event):
        axs2.clear()
        try: 
            float(rangeBoxHP.text)
        except:
            hoursP = 0
        else:
            hoursP = float(rangeBoxHP.text)

        try: 
            float(rangeBoxMP.text)
        except:
            minutesP = 0
        else:
            minutesP = float(rangeBoxMP.text)

        try: 
            float(rangeBoxSP.text)
        except:
            secondsP = 0
        else:
            secondsP = float(rangeBoxSP.text)  

        range2 = secondsP + 60*minutesP + 3600*hoursP


        i2=0
        j2=0
        if range2 < len(xP):
            while j2 < range2:
                i2 = i2+1
                j2 = xP[-1] - xP[-i2]  
        
        if i2 > len(xP):
            axs2.plot(xP,yP)
        else:
            axs2.plot(xP[-i2:],yP[-i2:])

    rangeBoxHP.on_submit(update)
    rangeBoxMP.on_submit(update)
    rangeBoxSP.on_submit(update)

    plt.show()
    return fig2, axs2, rangeBoxHP,rangeBoxMP, rangeBoxSP, ax_boxHP, ax_boxMP, ax_boxSP

rangeButton.on_clicked(pausedPlot)

def animate(k):
    latest_time = np.genfromtxt("test_decay.dat", usecols = 0)[-1]
    latest_temp = np.genfromtxt("test_decay.dat", usecols = 1)[-1]
   
    
    x.append(latest_time)
    y.append(latest_temp)    
    
    axs1.clear()
    
    try: 
        float(rangeBoxH.text)
    except:
        hours = 0
    else:
        hours = float(rangeBoxH.text)

    try: 
        float(rangeBoxM.text)
    except:
        minutes = 0
    else:
        minutes = float(rangeBoxM.text)

    try: 
        float(rangeBoxS.text)
    except:
        seconds = 0
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
