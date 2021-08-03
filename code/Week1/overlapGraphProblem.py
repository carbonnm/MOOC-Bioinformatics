""" Solve the Overlap Graph Problem (restated below).
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. 
     (You may return the nodes and their edges in any order.)
Note: You don't need to account for repeated elements in Patterns in this problem.
"""

def overlap(patterns):
    #I'll create a dictionnary to store each pattern with its adjacency list dedicated.
    #The advantage is the keys that help the storage. 
    dico = {}
    length = len(patterns[0])
    #We'll need a boucle to browse the patterns
    for i in range (len(patterns)):
        #We'll need a second one because we want to compare each pattern with the other ones
        #It sounds like it's going to introduce an O^2(n) complexity ... :/
        for j in range (len(patterns)):
            #Let's check if they are actually supposed to be in the adjacency list
            if patterns[i][1:length] == patterns[j][0:length - 1]:
                #Now we create a list for each key in case a key contains multiple elements
                dico.setdefault(patterns[i], [])
                if patterns[j] not in dico[patterns[i]]:
                    #Add it
                    dico[patterns[i]].append(patterns[j])
                
    #Let's print it
    for key, value in dico.items():
        print(key, '-->', value)

#Random test
print(overlap(["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT", "GGCAC"]))