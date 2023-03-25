
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

    
    def showPaths(self):

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
            distance[source] = 0

            max_distance = 0
            max_distance_node = (0, 0)
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
                        parent[nbr] = s
                        queue.append(nbr)
                        #distanceance of this vertex will be disstance of parentent +1 
                        distance[nbr] = distance[s]+1
                        #also check for maximum distanceance
                        if max_distance <= distance[nbr]:
                            max_distance = distance[nbr]
                            #this node will help in recreating the path
                            max_distance_node = nbr

                        #means we reached the end.
                        if y == 0 and reach == 0:
                            last_node = nbr
                            reach = 1

            #if we reached the end then we have to print this path 
            if reach == 1:
                didwereach = 1
                lastpathnode.append(source)
                path[source] = [last_node]

                temp_parent = parent[last_node]

                #path reconstruction from last node on path
                while(temp_parent != (-1, -1)):
                    path[source].append(temp_parent)
                    temp_parent = parent[temp_parent]
            #else we will print the longest shortest path 
            else:

                path[source] = [max_distance_node]

                temp_parent = parent[max_distance_node]

                #path reconstruction from last node on path
                while(temp_parent != (-1, -1)):
                    path[source].append(temp_parent)
                    temp_parent = parent[temp_parent]

        
        path_alledges = []
        #if we reaached the end we will only output the paths that reached the end .
        if didwereach == 1:
            for node in lastpathnode:
                for i in range(0, len(path[node])-1):
                    path_alledges.append(
                        ((path[node][i]), (path[node][i+1])))
        #if we didn't reach the end then we will print the longest shortest paths from each vertex 
        else:
            for k in range(0, self.vertices+1):
                node = (k, self.vertices)
                for i in range(0, len(path[node])-1):
                    path_alledges.append((
                        (path[node][i]), (path[node][i+1])))

        #first we colour all the nodes as red .
        nx.draw_networkx_nodes(self.G, pos=self.allpos,
                               node_size=1, node_color="red", label="points")
                               

        #then we colour all the edges in the graph as  red
        nx.draw_networkx_edges(
            self.G, pos=self.allpos, edgelist=self.alledges, edge_color="red", style='solid')
        #then we will coulour all the paths in the graph as green as told in  question 

        nx.draw_networkx_edges(
            self.G, pos=self.allpos, edgelist=path_alledges, edge_color="green", style='solid')

        plt.show()



if __name__ == "__main__":
    # Sample Test Case 1
    l = Lattice(26)
    l.show()

    # Sample Test Case 2
    l = Lattice(20)
    l.percolate(0.3)
    l.show()

    # Sample Test Case 3
    l = Lattice(21)
    l.percolate(0.5)

    # Sample Test Case 4
    l = Lattice(100)
    l.percolate(0.6)
    l.showPaths()

    # Sample Test Case 5
    l = Lattice(100)
    l.percolate(0.8)
    l.showPaths()
