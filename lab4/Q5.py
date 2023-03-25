import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

# diff method to calculate area under curve.
trapzivalues = []
simpsvalues = []
rombergvalues = []

# using 0 gives warning , maybe because python does some div operation with lower limit in linspace , so i am using 0.0001
points	 = np.linspace(0.0001, 1, 51)
realarea = []
#iterate on all 51 chosen points from 0 to 1
for i in points:
    #divide 0 to i in 11 parts 
    x_val = np.linspace(0, i, 11)

    #then applly different integration methods 
    rombergvalues.append(integrate.romberg(lambda x: 2*x*np.exp(x**2),0,i))

    trapzivalues.append(integrate.trapz((2*x_val*np.exp(x_val**2)), x=x_val))

    simpsvalues.append(integrate.simps((2*x_val*np.exp(x_val**2)), x=x_val))

    #exp(x^2) is the integration of asked function .
    realarea.append(np.exp(i**2)-1)

#plotting graph for visualization
plt.plot(points, realarea, label="real area", marker='*',color='red')
plt.plot(points, trapzivalues, label="Trapezoidal area", marker='x',color='green')
plt.plot(points, rombergvalues, label="Romberg area", lw=6)
plt.plot(points, simpsvalues, label="Simpson area", lw=2)
# labels and title
plt.ylabel("area of y(x)=2x.e^(x^2)")
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.title("plotting area under curve of y(x)=2x.e^(x^2) using scipy.integrate module")
# Showing graphics
plt.show()
