
"""
Below is the adjacency list that represents the graph of Iloilo Universities.

The graph is made to be traversable from one point to another.
"""
def set_graph():

    graph_km = {
        'A' : {'B' : 1.2 , 'C': 2.2, 'D' : 2.0},                #start node - UPV

        'B' : {'A' : 1.2, 'C': 0.3, 'D' : 0.55},                #USA

        'C' : {'B' : 0.3, 'D' : 0.25},                          #Assumption Iloilo

        'D' : {'C' : 0.25, 'E' : 1.3, 'F' : 1.7},               #St. Paul's

        'E' : {'D' : 1.2, 'F' : 0.5},                           #WIT

        'F' : {'E' : 1.2, 'G' : 0.9, 'H' :  1.4},               #WVSU

        'G' : {'H' : 0.45, 'F' : 0.9},                          #Collegio de San Jose

        'H' : {'I' : 1.3, 'G' : 0.45},                          #Saint Vincent Ferrer Seminary
        
        'I' : {'H' : 1.3},                                      #Goal Node - CPU 
        
        }
    
    return graph_km

def coordinates(node):

    match node:

        #UPV
        case 'A':
            return [10.698108775421403, 122.55547754462675]
        
        #USA
        case 'B':
            return [10.702199841325427, 122.56236990347229]
        
        case 'C':
            return [10.70188001238597, 122.56568846645919]
        
        case 'D':
            return [10.702115945215663, 122.56798284350869]
        
        case 'E':
            return [10.711069002902851, 122.56670318107837]
        
        case 'F':
            return [10.713856012683799, 122.56288379427703]
        
        case 'G':
            return [10.721547250653796, 122.56004524942976]
        
        case 'H':
            return [10.721833687480283, 122.55847496845799]
        
        case 'I':
            return [10.731472295086457, 122.54825537995497]

def get_school(node):

    match (node):

         #UPV
        case 'A':
            return 'University of the Philippines - Visayas'
        
        #USA
        case 'B':
            return 'University of San Agustin'
        
        case 'C':
            return 'Assumption Iloilo'
        
        case 'D':
            return 'St. Paul University'
        
        case 'E':
            return 'Western Institute of Technology'
        
        case 'F':
            return 'West Visayas State University'
        
        case 'G':
            return 'Colegio de San Jose'
        
        case 'H':
            return 'Saint Vincent Ferrer Seminary'
        
        case 'I':
            return 'Central Philippine University'
