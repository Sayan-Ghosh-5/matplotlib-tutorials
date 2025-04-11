import matplotlib.pyplot as plt
import numpy as np

#display multiple plots with subplots() can draw multiple plots in a single figure
#using subplots() method


plt.suptitle("multiple plots in a single figure")

#plot1
x= np.array([0,1,2,3])
y= np.array([1,3,5,7])

plt.subplot(2,2,1) # figure has 2 rows, 2 columns, plot 1 is used 
plt.plot(x,y)

plt.title("plot1")

#plot2

x = np.array([2,4,6,7])
y = np.array([2,5,9,8])

plt.subplot(2,2,2) # figure has 2 rows, 2 columns, plot 2 is used
plt.plot(x,y)
plt.title("plot2")
plt.show()



# subplot titles can be set using title() method
# big title can be set using suptitle() method
