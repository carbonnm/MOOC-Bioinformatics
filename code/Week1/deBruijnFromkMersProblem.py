""" DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.
    Input: A collection of k-mers Patterns.
    Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
"""

def deBruijnFromkMers(patterns):
    #As in the simple deBruijn problem, we'll need a dictionnary to store our final answer.
    adjacency = {}
    #We need to browse all the patterns
    for pattern in patterns:
        #We need to take the suffixes and prefixes of the pattern and make them keys in the dictionnary
        #Again, the [:-1] means that we only keep the k-1 meres
        key = pattern[:-1]
        #if the key is a new one, then let's add it in the dico, and make it a list to store
        #potentially multiple answers.
        if key not in adjacency:
            adjacency[key] = []
        #And now we'll add the value from 1 to the end of the pattern to the key.
        adjacency[key].append(pattern[1:])
    
    #Let's print the answer now
    for key, value in adjacency.items():
        print(key, "-->", value)


#Random test
print(deBruijnFromkMers(["GAGG","CAGG","GGGG","GGGA","CAGG","AGGG","GGAG"]))