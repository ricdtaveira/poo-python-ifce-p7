import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

print(xpoints)
print(ypoints)

plt.plot(xpoints, ypoints, 'o')
plt.show()