import numpy as np
import matplotlib.pyplot as plt

#integration of 2*x(e^(x^2)) is e^(x^2)
# so actual area is exp(9)-exp(1)
realarea = np.exp(9) - np.exp(1)

arealist = []

intervals = [i for i in range(1,31)]

#30 iterations to visualize trapezoidal rule, after each iteration we increase the number of interval's.
for i in range(1,31):
    # dividing range in i intervals
    x = np.linspace(1,3,i+1)

    # f(x) = 2*x.e^(x^2)
    fx = 2*x*np.exp(x**2)

    para_sum = 0
    #trapezoidal rule application
    for j in range(1,len(x)):
        para_sum += fx[j-1]+fx[j]
    
    # dist between pair of sides = (3-1)/i (cause 3-1 breaked in i parts)
    arealist.append(((3-1)*para_sum)/(2*i))

#for plotting the visualization.
plt.plot(intervals, arealist, label='trapezoidal area', color='red')
plt.axhline(realarea, label='actual area')
plt.legend()
plt.title("real area and trapezoidal area ")
plt.ylabel('Area')
plt.xlabel('Number of intervals')
plt.grid(True)
plt.show()
