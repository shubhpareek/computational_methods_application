
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random


#lattice class as asked in question 
class Lattice:
    #initialisations
    def __init__(self, n):
        #edges that are there in this grid
        self.alledges = []
        #will contain all the pointsin the grid
        self.allpos = {}
        #is the adjacency list of each point.
        self.adjacencylist = {}
        #num of vertices
        self.vertices = n

        #initialise the grid
        self.G = nx.grid_2d_graph(self.vertices+1, self.vertices+1)
        self.allpos = {(i, j): (i, j) for i, j in self.G.nodes()}


    # this function will jjust print the initial grid.

    def show(self):

        nx.draw_networkx_nodes(self.G, pos=self.allpos,
                               node_size=1, node_color="red", label="points")
        nx.draw_networkx_edges(
            self.G, pos=self.allpos, edgelist=self.alledges, edge_color="red", style='solid')
	

        plt.show()


    def percolate(self, p):

        # initializing adjacency list for each vertex
        for i in range(0, self.vertices+1):
            for j in range(0, self.vertices+1):
                self.adjacencylist[(i, j)] = []

        # traversing all the edges.
        for i in range(0, self.vertices+1):
            for j in range(0, self.vertices+1):
                pro = random.random()

                # adding edge to the right of point in graph with prob of 'p'
                if pro < p and i+1 <= self.vertices:
                    self.alledges.append(((i, j), (i+1, j)))
                    self.adjacencylist[(i, j)].append((i+1, j))
                    self.adjacencylist[(i+1, j)].append((i, j))

                pro = random.random()
                # adding edge to the left of point in graph with prob of 'p'
                if pro < p and j+1 <= self.vertices:
                    self.alledges.append(((i, j), (i, j+1)))
                    self.adjacencylist[(i, j)].append((i, j+1))
                    self.adjacencylist[(i, j+1)].append((i, j))

    
    def canwereachend(self):

        #distanceance from source 
        distance = {}
        #will store parentent of a vertex in a path
        parent = {}
        #will be used for bfs .
        visited = {}

        #if this is 1 it means we reached bottom.
        didwereach = 0
        #will be helpfull in recreating the path
        lastpathnode = []
        
        path = {}


        #we iterate on every vertex on top layer, then we will do bfs from it.
        for k in range(0, self.vertices+1):
            #initialisations 
            for i in range(0, self.vertices+1):
                for j in range(0, self.vertices+1):
                    visited[(i, j)] = 0
                    parent[(i, j)] = (-1, -1)
            
            
            #for bfs
            queue = []
            #source  is point (k,n)
            source = (k, (self.vertices))
            queue.append(source)
            visited[source] = True
           
            reach = 0
            last_node = (-1, -1)

            #bfs implementation
            while queue:
                s = queue.pop(0)

                #iterate on adjacency list of the source .
                for nbr in self.adjacencylist[(s)]:
                    #
                    (x, y) = nbr
                    if visited[nbr] == 0:
                        visited[nbr] = 1
                        queue.append(nbr)
                        
                        #means we reached the end.
                        if y == 0 and reach == 0:
                            reach = 1
                            return 1

        return 0
        
        
    #function for checking the given statement
    def statcheck(self, n):

        #100 equally space points from 0 to 1
        problist = np.linspace(0.0, 1.0, num=50)

        reachfractforprob = {}
        for p in problist:
            reachfractforprob[p] = 0
            #for every probabillity we will create 50 graphs and then check if we reached end
            for i in range(0, 50):
                g = Lattice(n)
                g.percolate(p)
                #if we reached end then increase fraction
                if g.canwereachend():
                    reachfractforprob[p] += 1
            #make average
            reachfractforprob[p] /= 50

        axisy = []
        axisx = []

        for key, value in reachfractforprob.items():
            axisx.append(key)
            axisy.append(value)

        plt.axvline(x=0.5, color="red", label="Percolation threshold")
        plt.plot(axisx, axisy, color="blue")
        plt.xlabel("p")
        plt.title("Critical cut-off in 2-D bond percolation")
        plt.ylabel("Fraction of runs end-to-end percolation occurred")
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()



if __name__ == "__main__":
    # Sample Test Case 1
    l = Lattice(10)
    l.statcheck(10)
