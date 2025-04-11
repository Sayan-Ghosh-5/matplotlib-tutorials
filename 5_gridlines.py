import matplotlib.pyplot as plt
import numpy as np

x = ([80,85,90,95,100,105,110,115,120])
y =([240,250,300,350,400,450,500,550,600])

#setting font properties via fontdict
font1 ={'family':'serif',
          'color':'blue',
          'weight':'bold',
          'size':10,
          }
font2 ={'family':'times new roman',
          'color':'red',
          'weight':'bold',
          'size':15,
          }

#can also change font position via loc

# adding grid lines by using grid() method


plt.plot(x,y)
plt.title("average heart rate vs average oxygen", fontdict=font2, loc="center")
plt.xlabel("average oxygen" , fontdict=font1, loc="left")
plt.ylabel("average heart rate", fontdict=font1, loc="bottom")

# plt.grid()

# specifying which grid lines to display via x axis or y axis
#plt.grid(axis='x')
# plt.grid(axis='y')

# specifying which grid lines to display via major or minor
# plt.grid(which='major')
# plt.grid(which='minor')

#specifing grid line color and style
plt.grid(color='blue', linestyle=':', linewidth=0.6)


plt.show()