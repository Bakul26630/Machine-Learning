# Generate different subplots from a given plot and color plot data.

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine

data = load_wine()
colors=["red","green","blue","yellow","maroon","darkblue","brown","darkblue","lightgreen","pink","purple","orange","teal"]
for i in range(0,12):
  plt.subplot(6,2,i+1)
  plt.plot(data.data[:,i],color=colors[i])
plt.suptitle("Feature Values Distribution through line chart")
plt.show()
