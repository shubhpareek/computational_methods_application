import random
import numpy as np
from numpy import append
import matplotlib.pyplot as plt

#this willl be used inside adjlist of vertices .
class adjacentnode:
    def __init__(self, value):
        self.next = None
        self.vertex = value


class UndirectedGraph:
    #initialisations for the graphh
    adjlist = {}
    edgesnumber = 0
    setofvertex = set()
    
    #if it's one it means graph is free .
    free = 1

    def __init__(self, V=-1):
        #check for free graph
        if V != -1:
            free = 0
            #add vetices in graph and initialise adjlist of each vertex
            for i in range(1, V+1):
                self.adjlist[i] = None
                self.setofvertex.add(i)
    

    #for printing the class .
    def __str__(self):
        print("Graph with ", len(self.setofvertex), " nodes and ",
              self.edgesnumber, ". Neighbors of the nodes are below:")

        #for printing as it is asked in the question .
        for i in self.setofvertex:
            neighbors = []
            temp = self.adjlist[i]

            while(temp is not None):
                neighbors.append(temp.vertex)
                temp = temp.next

            print("Node " + str(i) + ": {", end='')
            print(*neighbors, sep=",", end='')
            print("}")

        return ""
        
    #to add a new node to the graph .
    def addNode(self, new_vertex):

        try:
            #first we check for the presence of this vertex in graph, if already present we return it's adjacency list .
            if self.adjlist.get(new_vertex) is not None:
                return self.adjlist[new_vertex]
            #if we reach here it means vertex is not present in the graph, so then we check if graph is free or not , if it's free we do required initialisations.
            if self.free == 1:
                self.adjlist[new_vertex] = None
                return self.adjlist[new_vertex]
            #we reach here it  means that graph is not free .
            else:
                #then we check if the vertex getting added can be added , because it can't be greater than number of nodes already defined
                if new_vertex <= len(self.setofvertex):
                    self.adjlist[new_vertex] = None
                    return self.adjlist[new_vertex]
                else:
                    raise Exception(
                        "Node index cannot exceed number of nodes")

        except Exception as inst:
            print(type(inst))
            print(inst)

    # to add an edge to this graph
    def addEdge(self, a, b):
        #we create new nodes so that, older adjlist can be appended to it .
        node_a = adjacentnode(b)
        node_b = adjacentnode(a)
        #this will return the adjlist (if there) of a and b
        head_a = self.addNode(a)
        head_b = self.addNode(b)

        self.edgesnumber += 1
        
        #then we connect new values to the adjlist of a and  b
        node_a.next = head_a
        node_b.next = head_b
        self.adjlist[a] = node_a
        self.adjlist[b] = node_b

    #operator overloading for +
    def __add__(self, other):
        try:
            #then we check which type of + is it 
            #if it's a int then it means that we are adding an node.
            if(type(other) == int):
                self.addNode(other)
            #if it's  a tuple that means we are adding an edge
            elif(type(other) == tuple):
                (a, b) = other
                self.addEdge(a, b)
            else:
                raise Exception(
                    "Not appropriate overloading")

        except Exception as inst:
            print(type(inst))
            print(inst)

        return self


# This function will calculate the degree of vertices and then plot the graph of avg degree and fraction
# of vertices with a particular degree.


    def plotDegDist(self):
        sumofdeg = 0
        dicfordeg = {}
        #so we iterate on every vertex in graph and then calcualte its degree
        for i in self.setofvertex:
            degree = 0
            temp = self.adjlist[i]
            #iterating on adjacency list to calculate degree of this vertex
            while(temp is not None):
                degree += 1
                temp = temp.next

            #now we check, if this degree is already there or not , to update the fraction .
            if dicfordeg.get(degree) is not None:
                dicfordeg[degree] = dicfordeg[degree] + 1/len(self.setofvertex)
            else:
                dicfordeg[degree] = 1/len(self.setofvertex)

            #for calculating average degree.
            sumofdeg += degree
            avg_deg = sumofdeg/len(self.setofvertex)

        #now for plotting we will need x and y coordinates 
        xCord = []
        yCord = []

        #xcordinates will be the all the different degrees are there in graph and ycordinates will be the fraction of these degrees .
        for deg, frac in dicfordeg.items():
            xCord.append(deg)
            yCord.append(frac)

        #adding legends to the graph
        plt.ylabel("Fraction of nodes")
        plt.xlabel("Node degree")
        plt.title("Node Degree Distribution")

        
        #fix a line for average
        plt.axvline(x=avg_deg, c='red', label="Avg. node degree")
        
        #scatter plot
        plt.scatter(xCord, yCord, color="purple", marker='o',
                    label="Actual degree distribution")
                    
        plt.legend(loc='upper right')
        plt.grid(True)
        
        plt.show()
        
# the Class ERRandomGraph is a derived class from the Undirected class above.
# We add the edge between two vertices by random function , if random function returns a number less than P which means , probabillity of random number less than p is p. so it 
# does what is asked in the question .

class ERRandomGraph(UndirectedGraph):
    def sample(self, p):
        self.p = p
        for i in self.setofvertex:
            for j in range(1, i+1):
                if i == j:
                    continue
                t = random.random()
                # print(t)
                if t < p:
                    self.addEdge(i, j)

if __name__ == "__main__":
    # sample input
    g = ERRandomGraph(100)
    g.sample(0.5)
    g.plotDegDist()
    print(g)


