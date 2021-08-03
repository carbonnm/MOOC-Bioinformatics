""" String Composition Problem: Generate the k-mer composition of a string.
    Input: An integer k and a string Text.
    Output: Compositionk(Text), where the k-mers are arranged in lexicographic order.
"""

def kmersComposition(k, Text):
    #table declaration
    kmers = []
    #How to get the number of elements 
    numberElements = len(Text) - k + 1
    #for boucle who can go ahead the sequence and divide it
    for i in range(numberElements):
        #The divisions in elements
        element = Text[i:i + k]
        kmers.append(element)
    return kmers

#An example
print(kmersComposition(4,"CGAATATGGGGTGC"))