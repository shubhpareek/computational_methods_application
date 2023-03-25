import random
import matplotlib.pyplot as plt
import numpy as np
import math


# dice class
class dice:

    # sides of dice, 
    numofsides = 6
    #default value is 6
    #probabillity distribution for each side
    probdist = []
    #will store frequency of occurence of each side 
    freqofoc = []

    # this function is called as the object of the class is created.
    def __init__(self, numofsides=6):
        try:
            # check if given sides by the user is interger and greater than 4
            if (type(numofsides) is int) and (numofsides > 4):
                self.numofsides = numofsides
                # else raise exception
            else:
                raise Exception("Cannot construct the dice")
        except Exception as exceptinst:
            print(type(exceptinst))
            print(exceptinst)
            raise

    # this is utility function to see no. of sides of dice.
    def display(self):
        print("no. of sides = ", self.numofsides)

    # this is utility function sets the prob. of sides of dice.
    def setProb(self, distribution):
    
        sizoftuple = len(distribution)
        probSum = 0

        for prob in distribution:
            # print(prob)
            try:
                if prob < 0 or prob > 1:
                    raise Exception("Invalid probability distribution")

            except Exception as exceptinst:
                print(type(exceptinst))
                print(exceptinst)
                raise
                
            probSum = probSum+prob
        try:
            # checking if all the numofsides are not allocated or if sum of prob is not 1 then its a error.
            if probSum != 1 or sizoftuple != self.numofsides:
                raise Exception("Invalid probability distribution")

            # if all checks are passed then copy the provided probability array to the actual probability array
            self.probdist = np.copy(list(distribution))

        except Exception as exceptinst:
            print(type(exceptinst))
            print(exceptinst)
            raise

    # this function will roll the dice according to given distribution.
    def roll(self, n):

        # this is the freq that we will get .
        foundfreq = [0]*self.numofsides

        # this is the frequency that should have been by distribution 
        self.freqofoc = [x*n for x in self.probdist]


        # if roll func is called without giving any prob dist then it assumes uniform distribution
        if len(self.freqofoc) == 0:
            for i in range(n):
                self.freqofoc.append((1/self.numofsides)*n)
                self.probdist.append(1/self.numofsides)

        numberlist = []
        for i in range(1,self.numofsides+1):
            numberlist.append(i)
        
        #random.choices will do a sampling experiment according to given probdistribution
        occurence = random.choices(numberlist, weights=tuple(self.probdist), k=n)
        for i in occurence:
            foundfreq[i-1]+=1
        

        # position of both the bars
        displaybar1 = np.arange(self.numofsides)
        displaybar2 = [x+0.3 for x in displaybar1]

        # plotting of both the bars
        plt.bar(displaybar1, self.freqofoc, color='b', width=0.3, label="actual")
        plt.bar(displaybar2, foundfreq, color='g', width=0.3, label="expected")

        # marking the ith side no. on the x axis
        plt.xticks([r + 0.3 for r in range(self.numofsides)],
                   [x+1 for x in range(self.numofsides)])

        plt.legend()
        plt.show()

def main():
    obj = dice(6)
    obj.setProb((0.1, 0.1, 0.4, 0.2, 0.1, 0.1))
    obj.roll(100)
if __name__ == "__main__":
    main()
