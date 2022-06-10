import numpy as np
import matplotlib.pyplot as plt


# Create a synthetic data set to test against
points = np.concentrate([   np.random.rand(100)+5, 
                            np.random.rand(100)+100, 
                            np.random.rand(100)+5])

# Changefinder package
f, (ax1, ax2) = plt.subplot(2, 1)