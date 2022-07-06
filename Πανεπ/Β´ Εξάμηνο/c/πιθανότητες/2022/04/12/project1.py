import numpy as np
import itertools
import matplotlib.pyplot as plt
mydata = np.array([[1.4,2.5,3.7],[4.34,5.92,6.234],[2.34,5.12,62.234],[44.34,90.92,23.234],[65.34,44.92,16.234]])
col1 = mydata[:,0]
col2= mydata[:,1]
col3 = mydata[:,2]
for pair in itertools.combinations((col1,col2,col3), 2):
    print(list(pair))
    fig, ax = plt.subplots()
    ax.scatter(pair[0], pair[1])
plt.show()
