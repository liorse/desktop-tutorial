# draw a scatter plot of random data 2000 points in 3 dimensions using matplotlib
# and then use copilot to create a 3D scatter plot of the data

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# create a 3D scatter plot of random data
fig = plt.figure()

# create a 3D scatter plot of random data
ax = fig.add_subplot(111, projection='3d')

# create random data confined within a sphere of radius 10
x = np.random.normal(0, 10, 1000)
y = np.random.normal(0, 10, 2000)
z = np.random.normal(0, 10, 2000)

# plot the data make the dots blue and very small and confined within a sphere of radius 10
ax.scatter(x, y, z, c='b', marker='.', s=1)

# set the labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# set the title
ax.set_title('3D Scatter Plot')

# display the plot
plt.show()
