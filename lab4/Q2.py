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
#backward finite difference method
findiffback = (np.sin(x**2)-np.sin((x - h)**2))/h
#centered finite difference method
findiffcent = (findiff + findiffback)/2

#errors from true value of different method
findifer = abs(fdashx - findiff)
difbacker = abs(fdashx - findiffback)
cenerr = abs(fdashx - findiffcent)

#plotting diffferent approximations
plt.plot(x, cenerr, label='Centered finite difference approximation error')
plt.plot(x, difbacker, label='Backward finite difference approximation error')
plt.plot(x, findifer, label='Forward finite difference approximation error')

#legends
plt.title("plotting diffferent approximations")
plt.xlabel("x")
plt.ylabel("Errors")
plt.legend()
plt.grid(True)
plt.show()
