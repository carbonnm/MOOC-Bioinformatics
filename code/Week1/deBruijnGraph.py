"""  De Bruijn Graph from a String Problem: Construct the de Bruijn graph of a string.
     Input: An integer k and a string Text.
     Output: DeBruijnk(Text).
"""

def deBruijn(k, text):
     #Let's create a dictionnary because it seems like it would be easier with one
     adjacency = {}
     #We need to browse the text => for boucle
     for i in range(len(text) - k):
          #We need to indicate what our first k-mer will be
          #It will start at i and end k letters later.
          #For example, with our test, our first kmer will be AAG
          kmer = text[i:i+(k-1)]
          if kmer not in adjacency:
               #We will, just like in the previous exercise, create a list for each key,
               #in case there is multiple values for the same key.
               adjacency[kmer] = []
          #Now let's add the "graph" that the kmer follows 
          next = text[i+1:i+k]

          if len(next) == k - 1:
               #Add it
               adjacency[kmer].append(next)

     #Let's print the answer now
     for key, value in adjacency.items():
          print(key, "-->", value)

#Random test
print(deBruijn(4, 'AAGATTCTCTAAGA'))