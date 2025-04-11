# import matplotlib
# print(matplotlib.__version__)  # 3.7.1

import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1,2,4,8])
# ypoints = np.array([3,5,1,10])
# plt.plot(xpoints, ypoints,'o')


# xpoints = np.array([1,2,4,8])
# ypoints = np.array([3,5,1,10])

# plt.plot(xpoints, ypoints,'ro')

xpoints = np.array([3,10])
plt.plot(xpoints,marker='o')
plt.show()