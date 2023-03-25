from math import pi as PI
import matplotlib.pyplot as plt
import random

#this is a function to estimate pi by generating n points in the shape of a circle inscribed in a square .


def estimatePi(n):

    # initializing pts in circle and sq.
    insquare = 0
    insidecircle = 0

    # points for x axis 
    xaxis = []
    # values of pi found after number of iteration 
    estimatedVal = []

    # iterations of monte carlo experiment.

    for i in range(1,n+1):
    	#to get random points from the square
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2

        # if point lies inside circle.
        if distance <= 1:
            insidecircle += 1
        insquare += 1

        # estimate pi val after each iteration
        piVal = (insidecircle/insquare)
        piVal *= 4

        estimatedVal.append(piVal)
        xaxis.append(i)

    # plotting the pi vals.
    plt.title("Estimates π using Monte Carlo Method")
    plt.xlabel("No. of points generated")
    plt.ylabel("4 x fraction of points within the circle")
        
    plt.axhline(y=PI, c='r',label="value of pi")
    plt.plot(xaxis, estimatedVal, c='b',label="experimental pi")
    plt.legend(loc="lower right")
    plt.show()


def main():
    estimatePi(100000)
if __name__ == "__main__":
    main()
