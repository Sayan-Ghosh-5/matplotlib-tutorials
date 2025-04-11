# creating labesls for plot

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


plt.plot(x,y)
plt.title("average heart rate vs average oxygen", fontdict=font2, loc="center")
plt.xlabel("average oxygen" , fontdict=font1, loc="left")
plt.ylabel("average heart rate", fontdict=font1, loc="bottom")

plt.show()