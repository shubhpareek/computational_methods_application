
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


if __name__ == "__main__":
    # Sample Test Case 1
    r = RowVectorFloat([1, 2, 4])
    print(r)
    print(len(r))
    print(r[1])
    r[2] = 5
    print(r)

    r = RowVectorFloat([])
    print(len(r))

    # Sample Test Case 2
    r1 = RowVectorFloat([1, 2, 4])
    r2 = RowVectorFloat([1, 1, 1])
    r3 = 2 * r1 + (-3) * r2
    print(r3)
