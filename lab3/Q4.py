import matplotlib.pyplot as plt
import numpy as np

#class for polynomials
class Polynomial:
    #it will take coefficiants of polynomial as input for initialisation.
    def __init__(self, a):
        self.vec = list(a)
    #for printing the class 
    def __str__(self) -> str:
        #ex ->Coefficients of the polynomial are: -0.5 -1 -1.5
        print("Coefficients of the polynomial are:")
        for obj in self.vec:
            print(obj, end=' ')
        return ""

    #this will return value of p(x)
    def __getitem__(self, x):
        total = 0
        for i in range(0, len(self.vec)):
            total += self.vec[i]*(x**i)
        return total
    #to multiply a constant to a polynomial 
    def __rmul__(self, fac):
        tempppol = []
        #just iterate on coefficients and multiply.
        for i in range(0, len(self.vec)):
            tempppol.append(fac*self.vec[i])

        tempppol = Polynomial(tempppol)
        return tempppol

    #to multiply two polynomials 
    def __mul__(self, otherp):
        
        degDict = {}
        #initialising degrees that will be created by multiplication .
        for i in range(0, len(self.vec)):
            for j in range(0, len(otherp.vec)):
                degDict[i+j] = 0

        #basic multipllication implementation go on each degree of both then add the coefficiant to sum degree of resultant polynomial
        for i in range(0, len(self.vec)):
            for j in range(0, len(otherp.vec)):
                degDict[i+j] += self.vec[i]*otherp.vec[j]

        
        retPol = []
        #just converting the degree coeff in dic to rteturn polynomial.
        for key, val in degDict.items():
            retPol.append(val)

        retPol = Polynomial(retPol)
        return retPol

    #to add two polynomials
    def __add__(self, list1):
        
        l1 = len(list1.vec)
        l2 = len(self.vec)
        #in case they have different lengths 
        l3 = min(l1, l2)
        try:
            tempppol = []
            i = 0
            for i in range(0, l3):
                tempppol.append(self.vec[i]+list1.vec[i])

            #in case they have different lengths we adjust with adding 0.
            for i in range(l3, l1):
                tempppol.append(list1.vec[i])

            for i in range(l3, l2):
                tempppol.append(self.vec[i])

            tempppol = Polynomial(tempppol)
            return tempppol
        except Exception as inst:
            print(type(inst))
            print(inst)

    #to subtract two polynomial.
    def __sub__(self, list1):
        l1 = len(list1.vec)
        l2 = len(self.vec)
        #in case they have different length .
        l3 = min(l1, l2)
        try:
            #just subtractoin implementation .
            tempppol = []
            i = 0
            for i in range(0, l3):
                tempppol.append(self.vec[i]-list1.vec[i])

            #in case of different length one of the below loops will run .
            for i in range(l3, l1):
                tempppol.append(list1.vec[i])

            for i in range(l3, l2):
                tempppol.append(self.vec[i])

            tempppol = Polynomial(tempppol)
            return tempppol
        except Exception as inst:
            print(type(inst))
            print(inst)

    #to visualize the polynomial in a interval .
    def show(self, a, b):

        #take  (260 * numbers in range) equal spaced ,number of points from the range .
        x = np.linspace(a, b, 260*(b-a+1), endpoint=True) #np array

        y = 0
        for i in range(len(self.vec)):
            y += self.vec[i]*(x**i) #** is operator for np.power, * can be used to multiply on list in numpy.	

        plt.plot(x, y, '-g')

        plt.ylabel('P(x)')
        plt.xlabel('x')
        plt.title('curve for polynomial')
        plt.grid(True)
        plt.show()

    # given points for a polynomial we will use matrix method to fin 

    def fitViaMatrixMethod(self, pList):
        n = len(pList)
        # x and y list will store x and y from (x,y) given in pList
        y = []
        x = []
        mat = []
        for i in range(n):
            temp = [1]
            # storing values in mat, x and y
            for j in range(1, n):
                temp.append(pList[i][0]**j)
            y.append(pList[i][1])
            x.append(pList[i][0])
            mat.append(temp)

        # used np.linalg module to solve Ax = b and got x
        coeff = np.linalg.solve(mat, y)
        # updating coefs of polynomial
        self.vec = coeff

        # plotting given points
        plt.scatter(x, y, color='red')
        # finding range for x and creating x with 101 points withing range
        a = min(x)
        b = max(x)
        #take  (260 * numbers in range) equal spaced ,number of points from the range .
        x = np.linspace(a, b, 260*(b-a+1), endpoint=True)#np array

        yaxs = 0
        for i in range(n):
            yaxs += self.vec[i]*(x**i)

        plt.plot(x, yaxs, '-g')

        # giving labels and title to plot
        plt.ylabel('f(x)')
        plt.xlabel('x')
        plt.grid(True)
        plt.title("Polynomial interpolation using matrix method")
        plt.show()

    # langrange polynomial interpolation method implementation
    def fitViaLagrangePoly(self, pointL):
        n = len(pointL)
        # x and y list will store x and y from (x,y) given in pointL
        y = []
        x = []
        # resultant polynomial = total(yi*phi_i)
        # where phi_i = PI((x-xj)/(xi-xj)) for j in 1 to n where i!=j

        for i in range(n):
            p = Polynomial([1])
            # calculating PI((x-xj)/(xi-xj)) for j in 1 to n where i!=j
            for j in range(n):
                if(j == i):
                    continue
                # (x-xj) using - operator
                temp = Polynomial([])
                temp = Polynomial([0, 1])-Polynomial([pointL[j][0]])

                # dividing polynomial with (xi-xj) using * operator
                temp = (1/(pointL[i][0]-pointL[j][0]))*temp

                p = p * temp

            # multiplying resultant polynomial p with yi
            p = pointL[i][1]*p
            # adding x and y in lists
            y.append(pointL[i][1])
            x.append(pointL[i][0])

            # updating resultant polynomial by adding yi*phi_i for all i's
            if(i == 0):
                self = p
            else:
                self = self + p

        # plotting interpolation points
        plt.scatter(x, y, color='red')

        a = min(x)
        b = max(x)
        #take  (260 * numbers in range) equal spaced ,number of points from the range .
        x = np.linspace(a, b, 260*(b-a+1), endpoint=True)#np array
        yaxs = []
        for i in x:
            yaxs.append(self[i])

        # plotting x and yaxs
        plt.plot(x, yaxs, '-g')

        # giving labels and title to plot
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.title("Polynomial interpolation using matrix method")
        plt.show()


if __name__ == "__main__":
    #  Test Case 1
    p = Polynomial([1, 2, 3])
    print(p)

    #  Test Case 2
    p1 = Polynomial([1, 2, 4])
    p2 = Polynomial([4, 2, 1])
    p4 = p1 + p2
    print(p4)
    p4 = p1 - p2
    print(p4)

    #  Test Case 3
    p1 = Polynomial([1, 2, 4])
    p2 = (-0.5) * p1
    print(p2)

    #  Test Case 4
    p1 = Polynomial([-1, 1])
    p2 = Polynomial([1, 1, 1])
    p4 = p1 * p2
    print(p4)

    #  Test Case 5
    p = Polynomial([1, 2, 4])
    print(p[2])

    #  Test Case 6
    p = Polynomial([1, -1, 1, -1])
    p.show(-1, 2)

    #  Test Case 7
    p = Polynomial([])
    p.fitViaMatrixMethod([(1, 4), (0, 1), (-1, 0), (2, 15), (4, 12)])
    p.fitViaLagrangePoly([(1, 4), (0, 1), (-1, 0), (2, 15), (4, 12)])

    #  Test Case 8
    p = Polynomial([])
    p.fitViaLagrangePoly([(1, -4), (0, 1), (-1, 4), (2, 4), (4, 1)])
