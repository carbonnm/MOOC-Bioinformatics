"""Code Challenge: Solve the Eulerian Cycle Problem.
    Input: The adjacency list of an Eulerian directed graph.
    Output: An Eulerian cycle in this graph.
"""
def eulerianCycle(graph):
    #First, we are going to store for each node the number of edges that are emerging from them
    #That's why we'll need a dictionnary to store this information
    edges = {}
    #We need therefore to store in edges the len of the value that correspond in the list graph
    for i in range (len(graph)):
        edges[i] = len(graph[i])
    
    #Now that this is done, we'll need to store the circuit somewhere. I'll use a list
    #because keys will not be very useful.
    cycle = []
    #As I saw in the chapter, we are going to do kind of "backtracking" by testing randomly 
    #some cycles and see a bit what will happen en then act in consequence.
    #For this reason, we'll need to store a temporary cycle that will contain the cycle we are currently testing
    tempCycle = []

    #Now, we'll start from a random node. I'll chose number1 (because 0 may not be on each graph)
    node = 0
    tempCycle.append(0)

    #As said in the pseudocode given in the stepik intercative tool, the program needs to have
    #a while that will continue to boucle until there are no more inexplored edges in the graph
    while len(tempCycle):
        #We need now to see if there is an outdegree in the node chosen
        if edges[node]:
            tempCycle.append(node)
            #In that case, we'll go ahead and add the future node in our list, future nodes
            #that is given in the graph. The [-1] is again useful for not take the last list char
            #which is a special dedicated character.
            nextNode = graph[node][-1]
            #And then we need to remove it from the list of graph because otherwise we could
            #pass twice on the same spot.
            edges[node] -= 1
            graph[node].pop()

            #And now of course lets move on in the graph.
            node = nextNode
        
        #Now we need to manage the case where there is no more edges available,
        #which means that our cycle is not eulerian and that we have to find a newstart.
        else:
            #As I have seen in the explanations, i need to start from the cycle I formed,
            #and then make Cycle' <- Cycle as said in the pseudo code.
            #Cycle' and Cycle are our Cycle and tempCycle
            #Let's add a newStart as requested. 
            cycle.append(node)
            #Now we need to go back and make kindof backtracking.
            #The [-1] is for select the last element of tempCycle
            node = tempCycle[-1]
            #The new Start chosen, the tempCycle is no more useful, we'll just delete it
            #and try again to walk randomly from our newStart.
            tempCycle.pop()
    
    #Finally we have our final answer. Let's print it !
    #I had to read the range function documentation
    #The three arguments means the start, the stop and the step.
    #The -1 allow us to decrement because the list is now reversed.
    for i in range(len(cycle) - 1, -1, -1):
        print(cycle[i], end = "")
        print(" -> ", end = "")


#Random test

print(eulerianCycle([[3], [0], [1, 6], [2], [2], [4], [5, 8], [9], [7], [6]]))