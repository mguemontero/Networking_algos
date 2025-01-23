# Class to represent a graph
"""
    + Graph Class: A class to represent a graph with vertices (number of vertices) and graph (a list to store graph edges).
    + add_edge: A function to add an edge to the graph.
    +find: A function to find the subset of an element i.
    + union: A function to perform the union of two subsets.
    + kruskal_mst: The main function to construct the Minimum Spanning Tree using Kruskal's algorithm.
    
    Example Usage: An example usage of the Graph class to create a graph with 4 vertices and add edges between them. 
    Finally, the kruskal_mst function is called to find and print the MST.
    
    This code will output the edges included in the MST along with their weights.
"""
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  # Default dictionary to store the graph

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Function to find the subset of an element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Function to perform union of two subsets
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Function to construct MST using Kruskal's algorithm
    def kruskal_mst(self):
        result = []  # Store the resultant MST
        i = 0  # Index variable for sorted edges
        e = 0  # Index variable for result[]

        # Step 1: Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does not cause a cycle, include it in the result
            # and increment the index of the result for the next edge
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print the resultant MST
        print("Constructed MST:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")

# Example usage
if __name__ == "__main__":
    vertices = 4  # Number of vertices in the graph
    graph = Graph(vertices)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)

    graph.kruskal_mst()