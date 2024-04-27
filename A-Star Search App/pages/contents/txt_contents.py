
#about a*star search algp

def astar_content():

    content = 'The A* search algorithm, a widely used technique in finding the shortest path between nodes in a graph by balancing costs incurred so far and estimated to reach the goal, making it efficient in robotics, gaming, and route planning.\n\nIn the A* search algorithm, there is a relationship between the heuristic cost, total cost, and actual cost, which is crucial for guiding the search towards the goal efficiently while ensuring optimality.\n\nIn this project, A* Search Algorithm is an efficient algorithm that is used in GPS, Video games, and many more. This project will produce a program that is capable of using A* Search Algorithm to traverse a graph efficiently. We will use the University-walk graph and heuristics in Iloilo City that we created. '

    return content

def abt_map():

    content = 'The Graphs consist of a fixed node of the Universities that are located in Iloilo City. We used Google Maps to obtain the specific location and distance from each university. '

    return content

def a_cost():
    
    content = 'This represents the actual cost of reaching a particular node \( n \) from the start node along the current path. It measures the cumulative cost incurred so far in traversing the graph.'

    return content

def h_cost():

    content = 'This is an estimate of the cost from node \( n \) to the goal node. It provides a heuristic guide to the algorithm, helping it prioritize nodes that are closer to the goal. The heuristic function should be admissible (never overestimating the actual cost) and consistent (satisfying the triangle inequality).'

    return content

def f_cost():

    content = 'This is an estimate of the cost from node \( n \) to the goal node. It provides a heuristic guide to the algorithm, helping it prioritize nodes that are closer to the goal. The heuristic function should be admissible (never overestimating the actual cost) and consistent (satisfying the triangle inequality).'

    return content