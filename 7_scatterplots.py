import matplotlib.pyplot as plt
import numpy as np

'''x= np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y= np.array([99,86,87,88,100,86,103,87,94,78,77,85,86])

plt.scatter(x,y)
plt.show()'''

#comparing 2 plots on same graph 

#day1
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([100,105,84,87,100,86,103,87,94,78,77,85,86])
plt.scatter(x,y, color='green', label='day1')

#day2
x = np.array([2,2,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,98,112,103,111,92,99,78,77,85])
plt.scatter(x,y, color='pink', label='day2')

#we can give different colors to different plots using color parameter then call it in scatter() method
#by defalt red color is used for first plot and blue for second plot 


plt.title("scatterplot")
plt.show()


