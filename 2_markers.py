import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1,3,4,5])
# plt.plot(xpoints, marker="o")
# plt.show()

#  line refere•nce
# -  solid line
# : dotted
# -- dashed line
# -. dashline/ dotted line

# color reference
# r red
# g green
# b blue
# c Cyan
# m magenta
# k black
# y yellow
# w white

# ms is for marker size
# lw is for line width 
# alpha is for transparency
# linestyle is for line style
# marker is for marker style
# mec is for marker edge color
# mfc is for marker face color

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker="o", ms=10, linestyle='--',markeredgecolor='r',  markerfacecolor='b')
plt.show()