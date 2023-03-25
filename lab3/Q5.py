
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, Akima1DInterpolator,barycentric_interpolate
import numpy as np
from matplotlib.animation import FuncAnimation

# creating figure with specified limits on x and y
fig = plt.figure()
axis = plt.axes(xlim=(-0.05, 1.05), ylim=(-4.5, 4.5))

# four plot lines
Akimainter, = axis.plot([], [], lw=2, color="green", label="Akima")
cubicsplininter, = axis.plot([], [], lw=2, color="red", label="Cubic Spline")
baryinter, = axis.plot([], [], lw=2, color="purple", label="Barycentric")
origval, = axis.plot([], [], lw=2, color="blue", label="True")



# init function to initialise lines
def init():
    origval.set_data([], [])
    cubicsplininter.set_data([], [])
    Akimainter.set_data([], [])
    baryinter.set_data([], [])
    return origval, cubicsplininter, Akimainter, baryinter

# animater function will be passed as the func parameter in funcanimate
# and  calculates curves for diff interpolation techniques

def animater(i):

    # 1001 point from the range 0 to 1
    x = np.linspace(0.0, 1.0, 1001)

    # interpolation methods
    # tan(x)*sin(30x)*e^(x) for all values in x
    y_true = [np.tan(j)*np.sin(30*j)*np.exp(1)**j for j in x] 

    # for each frame iteration we ,sample to interpolate upon of size i+2 including 0 
    # and 1 and their y values
    x_sample = np.linspace(0.0, 1.0, i+2)
    y_sample = [np.tan(j)*np.sin(30*j)*np.exp(1)**j for j in x_sample] 

    # getting curve from Akima
    akima = Akima1DInterpolator(x_sample, y_sample)

    # getting y values from akima
    y_akima = akima(x)
    
    # getting curve from cubic spline interpolation
    cs = CubicSpline(x_sample, y_sample)

    # getting y values from cs
    y_cubicS = cs(x)
    
    # getting y values from barycentric interpolation
    y_barycentric = barycentric_interpolate(x_sample, y_sample, x)

    # Labelling the plot
    title = 'Different interpolations of tan(x).sin(30x).e^x for '
    title += str(i)+' samples'
    plt.title(label=title)

    # updating respective plots and returning them in each frame
    Akimainter.set_data(x, y_cubicS)
    cubicsplininter.set_data(x, y_barycentric)
    origval.set_data(x, y_true)
    baryinter.set_data(x, y_akima)
    return origval, cubicsplininter, Akimainter, baryinter


# label for axis and curves and showing grid
plt.grid(True)
plt.ylabel("f(x)")
plt.xlabel("x")
plt.legend()

#  37 frames with a delay of 200ms between each frame.
anim = FuncAnimation(fig, animater, init_func=init, frames=37, interval=200)
plt.show()

