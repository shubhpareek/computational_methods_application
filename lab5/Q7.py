# importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
# creating custom exception class to raise


def FASTFOURIERTRANSFORM(n):
    # CHECKING IF N IS POSITIVE AND A INTEGER .
    try:
        if(type(n) != int or n < 0):
            # raise exception()
            raise Exception("valid n should be non negative integer")
    except Exception as inst:
        print(type(inst))
        print(inst)
        sys.exit(1)

    # ak and bk list of coeffs
    ak = []
    bk = []

    for k in range(1, n+1):
        # functions to calculate ak and bk
        def function1(x): return np.exp(x)*np.cos(k*x)
        def function2(x): return np.exp(x)*np.sin(k*x)

        # integrating functions for -pi to pi
        a, _ = integrate.quad(function1, -np.pi, np.pi)
        b, _ = integrate.quad(function2, -np.pi, np.pi)
        ak.append(a/np.pi)
        bk.append(b/np.pi)

    a0, _ = integrate.quad(lambda x: np.exp(x)/np.pi, -np.pi, np.pi)

    # printing coeff
    print(" a0 is ", a0)
    print("coeffs ak where k = 1->n are")
    print(ak)
    print("coeffs bk where k = 1->n are")
    print(bk)

    # x for plot
    x = np.linspace(-np.pi, np.pi, 201)

    y = np.exp(x)

    plt.plot(x, y, color="red", label="e^x function")
    y_fft = []

    for i in x:
        val = a0/2
        for k in range(n):
            val += ak[k]*np.cos((k+1)*i) + bk[k]*np.sin((k+1)*i)
        y_fft.append(val)

    plt.plot(x, y_fft, color="blue", label="calculated function")

    plt.title("approx of e^x by fft for n = "+str(n))
    plt.xlabel('x')
    plt.ylabel('fx')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # testing
    FASTFOURIERTRANSFORM(10)
