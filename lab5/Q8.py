import numpy as np
import math
from scipy.fft import fft, ifft
import random

# function to multiply 2 large n digit numbers


def MULTIPLYINLOGN(a, b):
    # lengths of a and b

    len_a = len(a)
    len_b = len(b)

    # taking max length of a, b
    l = 2*max(len_b, len_a)
    b.reverse()
    a.reverse()

    # adding zeros to make it uniform
    a = a + [0 for i in range(len_a, l)]
    b = b + [0 for i in range(len_b, l)]

    b = np.array(b)
    a = np.array(a)

    # doing fft on a
    x1 = fft(a)
    # doing fft on b
    x2 = fft(b)

    # multiplying both x1 and x2
    x3 = [x1[i]*x2[i] for i in range(len(x2))]

    x3 = np.array(x3)
    # getting polynomial back
    ans = ifft(x3)

    # takin the real part and multiplying it by 10^i
    a = ([round(ans[i].real, 4)*(10**i) for i in range(len(ans))])

    # returning the answer
    return sum(a)

if __name__ == "__main__":
    # testing
    a = [math.floor(random.random()*10) for i in range(50)]
    b = [math.floor(random.random()*10) for i in range(50)]
    # caculating decimal value
    av = 0
    bv = 0
    for i in a:
        av *= 10
        av += i
    for i in b:
        bv *= 10
        bv += i

    # true multiplication
    ORIGINAL = av*bv
    # from fft and ifft
    CALCULATED = MULTIPLYINLOGN(a, b)

    # printing both values using scientific notation
    print("true value:", "{:e}".format(ORIGINAL))
    print("val from fft:", "{:e}".format(CALCULATED))
