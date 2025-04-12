#we will make bars in this
import matplotlib.pyplot as plt
import numpy as np

'''x= np.array(["a", "b", "c", "d"])
y= np.array([3, 7, 5, 8])
plt.bar(x,y)
plt.show()'''

#horizontal bar
'''x= np.array(["a", "b", "c", "d"])
y= np.array([3, 7, 5, 8])
plt.barh(x,y)
plt.show()'''

'''x= np.array(["a", "b", "c", "d"])
y= np.array([3, 7, 5, 8])
plt.bar(x,y, color="red", edgecolor="black", linewidth=2, alpha=0.5)
plt.show()'''

x= np.array(["a", "b", "c", "d"])
y= np.array([3, 7, 5, 8])
plt.bar(x,y, width=0.2)
plt.barh(x,y, height=0.2)
plt.show()