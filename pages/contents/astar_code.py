import heapq

class AStarGraph(object):
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics

    def get_neighbors(self, node):
        return self.graph.get(node, {})

    def a_star_algorithm(self, start, end):
        open_list = set([start])
        closed_list = set([])
        g = {}  # Actual movement cost to each position from the start position
        parents = {}  # Parents contains an adjacency map of all nodes

        # Default value if the node is not found in the graph
        g[start] = 0
        # Start node is in the open list
        parents[start] = None

        while len(open_list) > 0:
            n = None

            # Find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.heuristics[v] < g[n] + self.heuristics[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # If the current node is the end node
            if n == end:
                reconst_path = []

                # Change the condition to check for None instead of n
                while parents[n] is not None:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)
                reconst_path.reverse()

                return reconst_path


            # For all the neighbors of the current node
            for (m, weight) in self.get_neighbors(n).items():
                # If the current node is not present in both open_list and closed_list
                # Add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # Otherwise, check if it's quicker to first visit n, then m
                # And if it is, update parent data and g data
                # And if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # Remove n from the open_list, and add it to closed_list
            # Because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    
    def results(self, start, end):
        path = self.a_star_algorithm(start, end)
        if path is not None:
            # Calculate the actual cost by summing the weights of the edges between nodes in the path
            actual_cost = sum([self.graph[path[i]][path[i + 1]] for i in range(len(path) - 1)])
            # The total cost is the actual cost plus the heuristic of the end node
            total_cost = actual_cost + self.heuristics[end]

            # Format the costs to two decimal places
            formatted_actual_cost = "{:.2f}".format(actual_cost)
            formatted_total_cost = "{:.2f}".format(total_cost)

            # Print the formatted costs
            print("Actual Cost: {} km".format(formatted_actual_cost))
            print("Total Cost (with heuristic): {} km".format(formatted_total_cost))

