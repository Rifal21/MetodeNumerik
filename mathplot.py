import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
  return (2*x**2) - (5*x)


x = np.linspace(-1,2,10000)

y = f(x)

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
 
# depict illustration
plt.xlim(-1, 2)

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.axvline(x=0, color='k', linestyle='--', ymin=0.05, ymax=0.95)
plt.axvline(x=1, color='k', linestyle='--', ymin=0.05, ymax=0.95)
plt.show()