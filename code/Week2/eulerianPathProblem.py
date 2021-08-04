
"""Code Challenge: Solve the Eulerian Path Problem.
    Input: The adjacency list of a directed graph that has an Eulerian path.
    Output: An Eulerian path in this graph.
"""

#I'm just going to re-use here the function eulerianCycle that I coded before.
def eulerianCycle(graph):
    edges = {}
    for i in range (len(graph)):
        edges[i] = len(graph[i])
    cycle = []
    tempCycle = []
    node = 0
    tempCycle.append(0)
    while len(tempCycle):
        if edges[node]:
            tempCycle.append(node)
            nextNode = graph[node][-1]
            edges[node] -= 1
            graph[node].pop()
            node = nextNode
        else:
            cycle.append(node)
            node = tempCycle[-1]
            tempCycle.pop()

    eularian = []
    for i in range(len(cycle) - 1, -1, -1):
        eularian.append(cycle[i])
    return eularian


#Here is our main function.
def eulerianPath(adjacency):
    #First of all, we need to identify the unbalanced nodes.
    outdegree = {}
    indegree = {}

    #Let's add the number of edges each by counting the indegree and the outdegree of each node.
    #First, let's add the outdegree in the edges list.
    for i in range (len(adjacency)):
        outdegree[i] = len(adjacency[i])
    print(outdegree)

    #For the indegree, lets transform the list of list into a single list of elements
    temporary = []
    for sublist in adjacency:
        for item in sublist:
            temporary.append(item)
    
    print(temporary)

    #Now that we have a simple list with just the different nodes that are reached by an edge,
    #we can simply count the occurences of each node in the temporary list. 
    #Thanks to that, we will finally have the indegree dico complete
    for i in range (len(temporary)):
        indegree[i] = temporary.count(i)
        
    print(indegree)

    #This is now awesome, we have all our degrees calculated. We now need to compare these two
    #dictionnarys to find the nodes that are unbalanced. After that, we'll create a connection between those two.
    problematicNodes = [node for node in outdegree if node in indegree and outdegree[node] != indegree[node]]
    print("Here are our two problematic values")
    print(problematicNodes)

    #The principle will now to connect those two nodes to make an eulerian cycle
    for node in problematicNodes:
        print(node)
        print(outdegree[node])
        print(indegree[node])
        if outdegree[node] < indegree[node]:
            outdegree[node] = outdegree[node] + 1
        else:
            indegree[node] = indegree[node] + 1
        
        print(node)
        #+We have of course to modify the adjacency itself. 
        if node == problematicNodes[0]:
            adjacency[problematicNodes[0]].append(problematicNodes[1])
    
    
    print("Here is the eulerian cycle with the indegree and outdegree that are similar")
    print(indegree)
    print(outdegree)
    print(adjacency)

    #Now, we can finally calculate an eulerian cycle with the function I coded before
    cycle = eulerianCycle(adjacency)
    print(cycle)
    
    #Finally, we simply need to put them in the right order to be a path and not a cycle
    #For that, we need to cut in the right place
    answer = []
    for i in range (len(cycle)):
        if cycle[i] == problematicNodes[1] and cycle[i - 1] == problematicNodes[0]:
            answer.append(cycle[i])
    for i in range(cycle[problematicNodes[1]] - 1, len(cycle)):
        answer.append(cycle[i])
    
    for i in range(1, cycle[problematicNodes[0]] + 1):
        answer.append(cycle[i])
    
    #Let's print the final answer
    for i in range (len(answer)):
        print(answer[i], end = "")
        print(" -> ", end = "")
    return answer
    


#Random test
#print(eulerianPath([[2], [3], [1], [0, 4], [], [], [3, 7], [8], [9], [6]]))
print(eulerianPath([[5], [6], [1], [4], [0], [2], []]))