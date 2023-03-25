import matplotlib.pyplot as plt
import math 
from typing import List


def logofstirling(n: int) -> float:
    """
    stirling(n) = sqrt(2πn) * (n \ e)ⁿ
    """
    return ((0.5) * (math.log(2 * math.pi) + math.log(n))) + (n * (math.log(n) - 1))

def main():
    
    
    logsum1toN = 0  # Σlog(i)
    """
    logofnfact = [Σlog(i)] where i ∈ [1, N]
    logofstnum = [log(stirling(i))] where i ∈ [1, N]
    diffoffast = logofnfact - logofstnum
    """
    logofnfact = []
    logofstnum = []
    diffoffast = []
    N = 1000000
    # calculating the logofnfact, logofstnum, and diffoffast lists
    for i in range(1, N + 1):  
        logsum1toN += math.log(i)
        logofnfact.append(logsum1toN)
        rVal = logofstirling(i)
        logofstnum.append(rVal)
        diffoffast.append(logsum1toN - rVal)
    
    # generating points from 1 to N for x-axis points
    onetoN = list(range(1, N + 1))

    #  plotting log of  stirling number and N!

    # Title and Labels 
    plt.title("Stirling's approximation")
    plt.ylabel("log(nfact)  and  log(stirling)")
    plt.xlabel("N")

    # Plotting n vs log(n!)
    plt.plot(onetoN, logofnfact, "b", lw="5", label="logof(n!)")

    # Plotting n vs log(stirling(n))
    plt.plot(onetoN, logofstnum, ":r", lw="2", label="logof(stirling(n))")

    # Displaying the plot
    plt.legend()
    plt.show()

    # Plotting difference of factorial of n and stirling number 

    # title and labels
    plt.title(" Stirling's approximation compared to N!" )
    plt.xlabel("one to N" )
    plt.ylabel("difference")

    # Plotting log(n!) - log(stirling(n))
    plt.plot(onetoN,diffoffast,"ob",lw="4", label="logofN! - logofstirlingnum")
    plt.grid()

    # Displaying the plot
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
