# Create various type of plots/charts like histograms, plot based on sine/cosine function based on
# data from a matrix. Further label different axes in a plot and data in a plot.

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine

data = load_wine()
Y_val=[0,0,0]
for i in data.target:
  if i==0:
    Y_val[0]+=1
  elif i==1:
    Y_val[1]+=1
  else:
    Y_val[2]+=1
X=data.target_names

# Pie Chart
plt.pie(Y_val,labels=X,explode=[0.2,0.1,0],shadow=True)
plt.title("Pie Chart Showing the number of records in all three classes")
plt.legend(title="Three-Classes",loc=3)
plt.show()

# Bar Graph
plt.bar(X,Y_val,color=["red","blue","green"],width=0.3)
plt.xlabel("Classes")
plt.ylabel("Count of records in classes")
plt.title("Bar Graph Showing the number of records in all three classes")
plt.show()

# Histogram
plt.hist(np.random.normal(200,10,100))
plt.title("Histogram")
plt.show()

# Line Chart
plt.plot(data.data)
plt.legend(np.arange(1,13),title="Attributes")
plt.show()


# Sine Graph
X=np.array(data.data[:,2])
Y=np.sin(X)
plt.plot(X,Y,color="maroon")
plt.xlabel("Feature-3 Values")
plt.ylabel("Feature-3 Sine Values")
plt.title("Sine graph for Feature-3")
plt.show()

# Cosine Graph
X=np.array(data.data[:,5])
Y=np.cos(X)
plt.plot(X,Y,color="purple")
plt.xlabel("Feature-6 Values")
plt.ylabel("Feature-6 Cosine Values")
plt.title("Cosine graph for Feature-3")
plt.show()
