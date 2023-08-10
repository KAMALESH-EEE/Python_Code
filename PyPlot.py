import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0,2,5,6,3,7,89,34,23,45,87])

plt.pie(ypoints)
plt.show()