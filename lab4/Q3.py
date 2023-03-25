import numpy as np
import matplotlib.pyplot as plt

#take 100 equal spaced points from 0 to 1 .
x = np.linspace(0, 1, 100)

#derivative of sin(x^2) is 2xcos(x^2)
fdashx = 2*x*np.cos(x**2) #np.cos will apply cos on full np x array

#sellect 100 equal spaced hval's for the experiment
h_val = np.linspace(0.01,0.6,100)

#list for max absolute err on delta plus method
err_delta_plus = []
#list for max absolute err on delta centered method
err_centered = []
#list for max absolute err on theoretical value delta plus method
deltapluserrtheo = []
#list for max absolute err on theoretical value delta centered method
theoerrcentered = []

#will be used to calculate theoretical approximation error for delta centered
def delta_centered_err(x, h):

    left = x-h
    right = x+h
    x_h = np.linspace(left, right, 20)
    theo_centered = np.abs(((h**2)/6)*((-1*(8*(x_h**3))*np.cos(x_h**2))-(12*x_h*np.sin(x_h**2)))) #numpy .sin , .cos will apply on all x values 
    return max(theo_centered)
    
#will be used to calculate theoretical approximation error for delta plus
def delta_plus_err(x,h):
    
    c_h = np.linspace(x, x+h, 10)
    theo_delta_plus = np.abs(((h)/2)*(2*np.cos(c_h**2)-(4*(c_h**2))*np.sin(c_h**2))) #numpy .sin , .cos will apply on all x values
    return max(theo_delta_plus)
    
#iterate on h_val's
for h in h_val:
    #forward
    findiff = (np.sin((x + h)**2)-np.sin(x**2))/h #numpy .sin will apply on all x values 
    #backward
    difbacker = (np.sin(x**2)-np.sin((x - h)**2))/h
    #centered
    difforw = (findiff + difbacker)/2

    #max difference in realderivative vs the forward and centered
    err_delta_plus.append(np.max(abs(fdashx - findiff)))
    err_centered.append(np.max(abs(fdashx - difforw)))

    currdeltaplus = []
    currdeltacentered = []

    #calculate the theoretical max for each x with h , for both methods
    for cx in x:
        currdeltaplus.append(delta_plus_err(cx,h))

        currdeltacentered.append(delta_centered_err(cx, h))

    #then choose the max of all values that we got .
    deltapluserrtheo.append(np.max(currdeltaplus))
    theoerrcentered.append(np.max(currdeltacentered))

plt.title("plotting the maximum absolute error of approximations and their theoretical values")
plt.plot(h_val, err_delta_plus,label='Maximum forward finite difference approximation error')
plt.plot(h_val, theoerrcentered,label='Maximum theoretical centered finite difference approximation error')
plt.plot(h_val, deltapluserrtheo, label='Maximum theoretical forward finite difference approximation error')
plt.plot(h_val, err_centered,label='Maximum centered finite difference approximation error')
plt.xlabel("h")
plt.ylabel("Errors")
plt.legend()
plt.grid(True)
plt.show()
