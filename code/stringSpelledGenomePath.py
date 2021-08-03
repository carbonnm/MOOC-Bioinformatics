"""String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.
    Input: A sequence path of k-mers Pattern1, … ,Pattern such that the last k - 1 symbols 
    of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
    Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal 
    to Patterni (for 1 ≤ i ≤ n).
"""


#This function will combine the patterns given, it will be called by the pathToGenome function.
def combinaisonOfPath(part, paths):
    #Let's go through all the elements that are in the path list
    for element in paths:
        #Here goes the difficult part..
        #The goal is to find overlappings between the reads, that are here represented by part and element
        #As it is said in the statement, we need to find a pattern such that k - 1 last letters
        #from part are similar to k + 1 first letters from element. And that is what we are
        #checking here in this condition. 
        #PS : [:-1] in Python is used to remove the newline character that appears at the end of a string
        #     It is usefull to assemble the rest of the genome step by step. 
        #     The [-1] means that we want the last letter of the element. 
        #     Thanks to this [-1] we'll be able to construct the final genome nucleotide by nucleotide.

        if(part[len(part) - len(element) + 1:] == element[:-1]):
            part += element[-1]
    return part

#This function will return the final Genome 
def pathToGenome(path):
    #We will step by step build the genome
    part = ""
    part += path[0]
    #Let's use this function that will "overlap" the differents reads.
    genome = combinaisonOfPath(part, path[1:])
    return genome

#Random test
print(pathToGenome(["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]))