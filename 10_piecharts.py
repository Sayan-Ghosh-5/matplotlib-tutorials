#creating piecharts using pie method
import matplotlib.pyplot as plt
import numpy as np

'''y= np.array([11,12,33,24])
mylabels=["apple","banana","cherry","orange"]
# plt.pie(y)
plt.pie(y, labels=mylabels)
plt.show()'''

#start angle parameter
#default is 0 degrees at x axis, start angle can be changed using startangle parameter 

'''y= np.array([11,12,33,24])
mylabels=["apple","banana","cherry","orange"]   
plt.pie(y, labels=mylabels, startangle=90)
plt.show()  '''

# how to explode a slice of pie chart

'''y= np.array([11,12,33,24])
mylabels=["apple","banana","cherry","orange"]   
myexplode = [ 0.08, 0, 0.09, 0] # explode first slice of pie chart
plt.pie(y, labels=mylabels, explode=myexplode)  
plt.show()
'''

#making shadow for creativity and making beautiful
'''y= np.array([11,12,33,24])
mylabels=["apple","banana","cherry","orange"]   
myexplode = [ 0.08, 0, 0.09, 0] # explode first slice of pie chart
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)  
plt.show()'''

y= np.array([11,12,33,24])
mylabels=["apple","banana","cherry","orange"]   
myexplode = [ 0.08, 0, 0.09, 0] # explode first slice of pie chart
mycolors = ['red', 'blue', 'green', 'yellow'] # colors of pie chart slices

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True,colors=mycolors)
plt.title("pie chart") 
plt.legend(title="fruits", loc="upper right") # legend for pie chart
plt.axis('equal') # equal aspect ratio ensures that pie chart is circular
plt.show()
