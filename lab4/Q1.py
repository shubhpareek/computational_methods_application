import numpy as np
from matplotlib import markers
from cProfile import label
import matplotlib.pyplot as plt

#take 100 equal spaced points from 0 to 1 .
x = np.linspace(0, 1, 100)

#derivative of sin(x^2) is 2xcos(x^2)
fdashx = 2*x*np.cos(x**2) #np.cos will apply cos on full np x array

#as said in question we have to take 0.01
h = 0.01

#forward finite difference method
findiff = (np.sin((x + h)**2)-np.sin(x**2))/h 

#plot finite difference against , true derivative.
plt.plot(x, fdashx, '--or',label='True derivate')
plt.plot(x, findiff,label="Forward finite difference approximation", marker='*')

#legends
plt.xlabel("x")
plt.ylabel("Derivates")
plt.title("forward finited difference against true derivative")
plt.legend()
plt.grid(True)
plt.show()
