"""Code Challenge: Solve the Eulerian Path Problem.
    Input: The adjacency list of a directed graph that has an Eulerian path.
    Output: An Eulerian path in this graph.
"""

def eulerianPath(adjacency):
    #First of all, we need to identify the unbalanced nodes.
    edge = {}

    #Let's add the number of edges each by counting the indegree and the outdegree of each node.
    #First, let's add the outdegree in the edges list.
    for i in range (len(adjacency)):
        edge[i] = len(adjacency[i])
    print(edge)

#Random test
print(eulerianPath([[2], [3], [1], [0, 4], [], [], [3, 7], [8], [9], [6]]))