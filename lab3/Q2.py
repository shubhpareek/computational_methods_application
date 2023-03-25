import random

#class created for row vector
class RowVectorFloat:
    #innitialisations for row vector.
    def __init__(self, a):
        self.vec = list(a)


    #this is overloader for accessing ith element
    def __getitem__(self, idx):
        return self.vec[idx]
        

    #this is overloader for setting ith element 
    def __setitem__(self, key, value):
        self.vec[key] = value
    
    #to print the class .
    def __str__(self) -> str:
        for ele in self.vec:
            print(ele, end=' ')
        return ""

    #overloader for scalar multiplication, returns the vector after multiplication 
    def __rmul__(self, fac):
        retlist = []
        for i in range(0, len(self.vec)):
            retlist.append(fac*self.vec[i])

        retlist = RowVectorFloat(retlist)
        return retlist


    #overloader for len function for this class 
    def __len__(self):
        return len(self.vec)

    #to add two vectors
    def __add__(self, list1):
        l1 = len(list1.vec)
        l2 = len(self.vec)
        #this will be helpfull if length of both vectors are not same , in that case we extend the vector with lesser length and we consider those dimensions filled with 0
        l3 = min(l1, l2)
        try:
            i = 0
            retlist = []
            
            #first we add the common length 
            for i in range(0, l3):
                retlist.append(self.vec[i]+list1.vec[i])

            #then we add the length that is left 
            for i in range(l3, l1):
                retlist.append(list1.vec[i])

            for i in range(l3, l2):
                retlist.append(self.vec[i])

            retlist = RowVectorFloat(retlist)
            return retlist
            
        except Exception as inst:
            print(type(inst))
            print(inst)



class SquareMatrixFloat:
    #list of RowVectorFloat
    def __init__(self, n):
        self.matrix = []
        #this list will be used to create RowVectorFloat object which will used in matrix
        tempList = [0 for i in range(0, n)]
        for i in range(0, n):
            obj = RowVectorFloat(tempList)
            self.matrix.append(obj)

    #to print the matrix 
    def __str__(self) -> str:
        print("The matrix is:")

        #print all rows of square matrix
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i].vec)):
                print(self.matrix[i].vec[j], end=' ')
            #next line after each row .
            print('')

        return ""

    #to get the ith row.
    def __getitem__(self, idx1):

        return self.matrix[0]

    #to sample a symmetric matrix .
    def sampleSymmetric(self):

        n = len(self.matrix)
        for i in range(0, n):
            for j in range(0, n):
                #as asked in question at the diagonal position the elements should be sampled from (0,n)
                if i == j:
                    #round function rounds the number to specified decimals , 2 in this case .
                    t = round(random.uniform(0, n), 2)
                    self.matrix[i].vec[j] = t
                #and if not diagonal element then it should be sampled from (0,1)
                else:
                    t = round(random.uniform(0, 1), 2)
                    self.matrix[i].vec[j] = t
                    self.matrix[j].vec[i] = t
    #to convert in row echelon form.
    def toRowEchelonForm(self):
        n = len(self.matrix)
        #iterate on each row 
        for i in range(0, n):
            #if the diagonal position is 0 then we check if there is some position in this column which is not 0
            if self.matrix[i].vec[i] == 0:
                found = 0
                for j in range(i+1, n):
                    #so if there is a position in column which is not 0 we swap it with our row and break.
                    if self.matrix[j].vec[i] != 0:
                        self.matrix[i], self.matrix[j] = self.matrix[j], self.matrix[i]
                        found = 1
                        break
                #if all column below is already 0 then we do nothing .
                if found == 0 or self.matrix[i].vec[i] == 0:
                    continue
            #now we make column below our point to be 0 .
            for j in range(i+1, n):
                e1 = self.matrix[i].vec[j]
                e2 = self.matrix[i].vec[i]
                #just row subtraction to make left leading point 0.
                b = self.matrix[i].vec[j]/self.matrix[i].vec[i]
                b = e1/e2
                tempL = (-b*(self.matrix[i]))
                self.matrix[j] = self.matrix[j] + tempL

            self.matrix[i] = (1/self.matrix[i][i])*self.matrix[i]
            
            #just rounding again in case.
            for i in range(0, n):
                for j in range(0, n):
                    self.matrix[i][j] = round(self.matrix[i][j], 2)

    def isDRDominant(self):
        n = len(self.matrix)

        #iterate on every row
        for i in range(0, n):
            sum = 0
            for j in range(0, n):
                if i != j:
                    sum += self.matrix[i][j]
            #just checking if it is row dominant or not
            if self.matrix[i][i] < sum:
                # print(sum)
                return False

        return True

    #jacobian Ax = b ,
    def jSolve(self, b, m):
        n = len(self.matrix)
        try:
            
            #jacobian implementation
            if self.isDRDominant():

                #Xk-1
                p = [0 for i in range(0, n)]
                c = []
                err = []
                # do this for m iterations.
                for k in range(0, m):

                    for i in range(0, n):
                        a = self.matrix[i].vec
                        sum = 0
                        for j in range(0, n):
                            if j != i:
                                sum += a[j]*p[j]
                        #ele is the Xi in the jacobian conversion formula
                        ele = (b[i]-sum)/a[i]
                        c.append(ele)

                    rowSum = 0
                    #first we  calculate variance from sollution  then we convert it to deviation 
                    for i in range(0, n):
                        a = self.matrix[i].vec
                        diff = -b[i]
                        for j in range(0, n):
                            diff += a[j]*p[j]

                        rowSum += diff**2
                    #err will contain deviation after each iteration
                    err.append(rowSum**(0.5))

                    
                    p = c #from Xk-1 to Xk
                    c = []

                return (err, p)

            else:
                raise Exception("matrix is not DDR or not convergent")

        except Exception as inst:
            print(type(inst))
            print(inst)
            return ([],[])

    #gauss siedel
    def gsSolve(self, b, m):
        n = len(self.matrix)
        try:
            #checking row dominance
            if self.isDRDominant():

                p = [0 for i in range(0, n)]
                c = []
                err = []
                #m iterations
                for k in range(0, m):

                    for i in range(0, n):
                        a = self.matrix[i].vec

                        sum1 = 0
                        for j in range(0, i-1):

                            sum1 += a[j]*c[j] # c is the xKj where j from(0,i-1)

                        sum2 = 0
                        for j in range(i+1, n):
                            sum2 += a[j]*p[j] # p is the xKi where i from (i+1,n)

                        ele = (b[i]-sum1 - sum2)/a[i]

                        c.append(ele)

                    rowSum = 0
                    #first we  calculate variance from sollution  then we convert it to deviation 
                    for i in range(0, n):
                        a = self.matrix[i].vec
                        diff = -b[i]
                        for j in range(0, n):
                            diff += a[j]*p[j]

                        rowSum += diff**2
                    #err will contain deviation after each iteration
                    err.append(rowSum**(0.5))

                    
                    p = c #from Xk-1 to Xk
                    c = []

                return (err, p)

            else:
                raise Exception("matrix is not DDR or not convergent")

        except Exception as inst:
            print(type(inst))
            print(inst)
            return ([],[])

if __name__ == "__main__":
    # Sample Test Case 1
    s = SquareMatrixFloat(3)
    print(s)

    # Sample Test Case 2
    s = SquareMatrixFloat(4)
    s.sampleSymmetric()
    print(s)

    # Sample Test Case 3
    s = SquareMatrixFloat(4)
    s.sampleSymmetric()
    print(s)
    s.toRowEchelonForm()
    print(s)

    # Sample Test Case 4
    s = SquareMatrixFloat(4)
    s.sampleSymmetric()
    print(s.isDRDominant())
    print(s)

    # Sample Test Case 5
    s = SquareMatrixFloat(4)
    s.sampleSymmetric()
    while not s.isDRDominant():
        s.sampleSymmetric()

    (e, x) = s.jSolve([1, 2, 3, 4], 10)
    print(x)
    print(e)

    # Sample Test Case 6
    s = SquareMatrixFloat(4)
    s.sampleSymmetric()
    while not s.isDRDominant():
        s.sampleSymmetric()

    (e, x) = s.gsSolve([1, 2, 3, 4], 10)
    print(x)
    print(e)
