"""Code Challenge: Solve the String Reconstruction Problem.
Input: An integer k followed by a list of k-mers Patterns.
Output: A string Text with k-mer composition equal to Patterns. 
(If multiple answers exist, you may return any one.)
"""

#This problem is a great summary of all the problems I already solved.

#Here's my deBruijn function without comments

def deBruijn(patterns):
    adjacency = {}
    for pattern in patterns:
        key = pattern[:-1]
        if key not in adjacency:
            adjacency[key] = []
        adjacency[key].append(pattern[1:])
    #I'll just had this part in my dico, to make it easier the eularian path
    for pattern in patterns:
        key = pattern[1:]
        if key not in adjacency:
            adjacency[key] = []

    for key, value in adjacency.items():
        print(key, "-->", value)
    return adjacency

#Here are the eularian related functions without any comments
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

def eulerianPath(adjacency):
    outdegree = {}
    indegree = {}
    for i in range (len(adjacency)):
        outdegree[i] = len(adjacency[i])
    temporary = []
    for sublist in adjacency:
        for item in sublist:
            temporary.append(item)
    for i in range (len(temporary)):
        indegree[i] = temporary.count(i)
    problematicNodes = [node for node in outdegree if node in indegree and outdegree[node] != indegree[node]]
    for node in problematicNodes:
        if outdegree[node] < indegree[node]:
            outdegree[node] = outdegree[node] + 1
        else:
            indegree[node] = indegree[node] + 1
        if node == problematicNodes[0]:
            adjacency[problematicNodes[0]].append(problematicNodes[1])
    cycle = eulerianCycle(adjacency)
    answer = []
    for i in range (len(cycle)):
        if cycle[i] == problematicNodes[1] and cycle[i - 1] == problematicNodes[0]:
            answer.append(cycle[i])
    for i in range(cycle[problematicNodes[1]] - 1, len(cycle)):
        answer.append(cycle[i])
    for i in range(1, cycle[problematicNodes[0]] + 1):
        answer.append(cycle[i])
    for i in range (len(answer)):
        print(answer[i], end = "")
        print(" -> ", end = "")


#Here are the functions I use for the String spelled genome path problem without comments

def combinaisonOfPath(part, paths):
    for element in paths:
        if(part[len(part) - len(element) + 1:] == element[:-1]):
            part += element[-1]
    return part

def pathToGenome(path):
    part = ""
    part += path[0]
    genome = combinaisonOfPath(part, path[1:])
    return genome


def stringReconstruction(k, patterns):
    dB = deBruijn(patterns)
    print(dB)
    #Now the problem is that we have a dictionnary and not a list of values and edges.
    #Let's wisely transform it into a list
    #This list will, for each k-mer, determines the occurences and we will be able to 
    #Let's just firts have a list where we can just list the k-mer
    kmer = []
    i = 0
    for key in dB.keys():
        kmer.append([key])
        i += 1
    print(kmer)
    #And now the final list
    adjacency = []
    #We'll just turn it into a list of string to compare it with 
    
    adjacency = list(dB.values())
    #Now let's add the correct correspondants.
    final = []
    for i in range (len(adjacency)):
        if adjacency[i] == []:
                final.append([])
        for j in range (len(kmer)):
            if adjacency[i] == kmer[j]:
                final.append([j])
    print(adjacency)
    print("This is the final answer that we're going to pass to the eulerian function")
    print(final)
    
    #Let's now use the eulerian function.
    eulerian = eulerianPath(final)
    

#Random test
print(stringReconstruction(4,["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"]))