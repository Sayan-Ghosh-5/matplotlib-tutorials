#histogram is a graphical representation of the distribution of numerical data showing frquency of data
#it is a type of bar plot where the x-axis represents the bins and y-axis represents the frequency of data in each bin
import matplotlib.pyplot as plt
import numpy as np

#hist() method is used to plot histogram
x =np.random.randn(1000) #1000 random numbers from standard normal distribution
plt.hist(x, bins=30, color='blue', edgecolor='black', alpha=0.5)
plt.show()