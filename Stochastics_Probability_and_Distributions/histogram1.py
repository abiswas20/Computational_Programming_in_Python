###Code below is based on Fig.15.18 in John Guttag's book.Gives us a very simple example of how to plot a histogram.###

import random
import matplotlib.pyplot as plt

vals=[]
for i in range (100000):
    num1=random.choice(range(0,101))   #chooses between 0 and 100#
    num2=random.choice(range(0,101))
    vals.append((num1+num2)/2)
plt.hist(vals,bins=50)
plt.ylabel('number of occurences')
plt.show()
