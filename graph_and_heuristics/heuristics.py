
"""

Below is the different heuristics that will be used to traverse the graph of Iloilo Universities

Different Heuristics will be used and depend on the goal node

"""

def set_heu(goal_node):

    #Assuming Goal Node is UPV, this is the heuristic
    upv_heu = {
        'A': 0,    # Estimated distance from 'A' to 'UPV' to itself (0 for the goal)
        'B': 0.9,  # Estimated distance from 'B' to 'UPV'
        'C': 1.6,  # Estimated distance from 'C' to 'UPV'
        'D': 1.8,  # Estimated distance from 'D' to 'UPV'
        'E': 2.6,  # Estimated distance from 'E' to 'UPV'
        'F': 3.1,  # Estimated distance from 'F' to 'UPV' 
        'G': 3.9,  # Estimated distance from 'G' to 'UPV'
        'H': 3.4,  # Estimated distance from 'H' to 'UPV'
        'I': 4.1,  # Estimated distance from 'I' to 'UPV'
    }

    #Assuming Goal Node is USA, this is the heuristic
    usa_heu = {
        'A': 1.0,  # Estimated distance from 'A' to 'USA' 
        'B': 0,    # Estimated distance from 'B' to 'USA' to itself (0 for the goal)
        'C': 0.3,  # Estimated distance from 'C' to 'USA'
        'D': 0.55, # Estimated distance from 'D' to 'USA'
        'E': 1.5,  # Estimated distance from 'E' to 'USA'
        'F': 2.1,  # Estimated distance from 'F' to 'USA' 
        'G': 3.0,  # Estimated distance from 'G' to 'USA'
        'H': 3.5,  # Estimated distance from 'H' to 'USA'
        'I': 4.7,  # Estimated distance from 'I' to 'USA'
    }

    #Assuming Goal Node is Assumption Iloilo, this is the heuristic
    assum_heu = {
        'A': 2.2,  # Estimated distance from 'A' to 'Assumption Iloilo' 
        'B': 0.3,  # Estimated distance from 'B' to 'Assumption Iloilo' 
        'C': 0,    # Estimated distance from 'C' to 'Assumption Iloilo' to itself (0 for the goal)
        'D': 0.25, # Estimated distance from 'D' to 'Assumption Iloilo'
        'E': 1.3,  # Estimated distance from 'E' to 'Assumption Iloilo'
        'F': 1.9,  # Estimated distance from 'F' to 'Assumption Iloilo' 
        'G': 2.6,  # Estimated distance from 'G' to 'Assumption Iloilo'
        'H': 3.1,  # Estimated distance from 'H' to 'Assumption Iloilo'
        'I': 5.8,  # Estimated distance from 'I' to 'Assumption Iloilo'
    }

    #Assuming Goal Node is St. Paul, this is the heuristic
    stp_heu = {
        'A': 2.0,  # Estimated distance from 'A' to 'St. Paul' 
        'B': 0.55, # Estimated distance from 'B' to 'St. Paul' 
        'C': 0.25, # Estimated distance from 'C' to 'St. Paul'
        'D': 0,    # Estimated distance from 'D' to 'St. Paul' to itself (0 for the goal)
        'E': 1.2,  # Estimated distance from 'E' to 'St. Paul'
        'F': 1.7,  # Estimated distance from 'F' to 'St. Paul' 
        'G': 2.5,  # Estimated distance from 'G' to 'St. Paul'
        'H': 2.9,  # Estimated distance from 'H' to 'St. Paul'
        'I': 5.6,  # Estimated distance from 'I' to 'St. Paul'
    }

    #Assuming Goal Node is WIT, this is the heuristic
    wit_heu = {
        'A': 2.4,  # Estimated distance from 'A' to 'WIT' 
        'B': 1.7,  # Estimated distance from 'B' to 'WIT' 
        'C': 1.6,  # Estimated distance from 'C' to 'WIT'
        'D': 1.8,  # Estimated distance from 'D' to 'WIT'  
        'E': 0,    # Estimated distance from 'E' to 'WIT' to itself (0 for the goal)
        'F': 0.5,  # Estimated distance from 'F' to 'WIT' 
        'G': 1.3,  # Estimated distance from 'G' to 'WIT'
        'H': 1.8,  # Estimated distance from 'H' to 'WIT'
        'I': 3.5,  # Estimated distance from 'I' to 'WIT'
    }

    #Assuming Goal Node is WVSU, this is the heuristic
    wvsu_heu = {
        'A': 2.9,  # Estimated distance from 'A' to 'WVSU' 
        'B': 2.1,  # Estimated distance from 'B' to 'WVSU' 
        'C': 2.5,  # Estimated distance from 'C' to 'WVSU'
        'D': 2.3,  # Estimated distance from 'D' to 'WVSU'  
        'E': 0.5,  # Estimated distance from 'E' to 'WVSU' 
        'F': 0,    # Estimated distance from 'F' to 'WVSU' to itself (0 for the goal) 
        'G': 0.8,  # Estimated distance from 'G' to 'WVSU'
        'H': 1.3,  # Estimated distance from 'H' to 'WVSU'
        'I': 3.0,  # Estimated distance from 'I' to 'WVSU'
    }

    #Assuming Goal Node is Colegio de San Jose, this is the heuristic
    csj_heu = {
        'A': 3.5,  # Estimated distance from 'A' to 'CSJ' 
        'B': 2.9,  # Estimated distance from 'B' to 'CSJ' 
        'C': 3.2,  # Estimated distance from 'C' to 'CSJ'
        'D': 3.1,  # Estimated distance from 'D' to 'CSJ'  
        'E': 1.3,  # Estimated distance from 'E' to 'CSJ' 
        'F': 0.5,  # Estimated distance from 'F' to 'CSJ' 
        'G': 0,  # Estimated distance from 'G' to 'CSJ' to itself (0 for the goal)
        'H': 0.45, # Estimated distance from 'H' to 'CSJ'
        'I': 2.2,  # Estimated distance from 'I' to 'CSJ'
    }

    #Assuming Goal Node is Saint Vincent Ferrer Seminary, this is the heuristic
    svfs_heu = {
        'A': 3.4,  # Estimated distance from 'A' to 'SVFS' 
        'B': 3.3,  # Estimated distance from 'B' to 'SVFS' 
        'C': 3.7,  # Estimated distance from 'C' to 'SVFS'
        'D': 3.9,  # Estimated distance from 'D' to 'SVFS'  
        'E': 1.8,  # Estimated distance from 'E' to 'SVFS' 
        'F': 1.4,  # Estimated distance from 'F' to 'SVFS' 
        'G': 0.45, # Estimated distance from 'G' to 'SVFS'
        'H': 0,    # Estimated distance from 'H' to 'SVFS' to itself (0 for the goal)
        'I': 1.8,  # Estimated distance from 'I' to 'SVFS'
    }

    #Assuming Goal Node is CPU, this is the heuristic
    cpu_heu = {
        'A': 3.9,  # Estimated distance from 'A' to 'CPU'
        'B': 4.4,  # Estimated distance from 'B' to 'CPU'
        'C': 4.8,  # Estimated distance from 'C' to 'CPU'
        'D': 5.0,  # Estimated distance from 'D' to 'CPU'
        'E': 3.6,  # Estimated distance from 'E' to 'CPU'
        'F': 2.7,  # Estimated distance from 'F' to 'CPU' 
        'G': 1.8,  # Estimated distance from 'G' to 'CPU'
        'H': 1.3,  # Estimated distance from 'H' to 'CPU'
        'I': 0,    # Estimated distance from 'I' to 'CPU' to itself (0 for the goal)
    }

    match goal_node:

        case 'A': #UPV
            return upv_heu
        
        case 'B': #USA
            return usa_heu
        
        case 'C': #Assumption Iloilo
            return assum_heu
        
        case 'D': # St. Paul
            return stp_heu
        
        case 'E': #WIT
            return wit_heu
        
        case 'F': #WVSU
            return wvsu_heu
        
        case 'G': #CSJ
            return csj_heu
        
        case 'H': #SVFS
            return svfs_heu
        
        case 'I': #CPU
            return cpu_heu
        
        case other:
            raise ValueError('Wrong Input')
        
    


