import sys

def tsp(graph, start):
    # Set up variables
    visited = set()
    path = [start]
    cost = 0
    
    # Visit all nodes
    while len(visited) < len(graph):
        current = path[-1]
        visited.add(current)
        
        # Find nearest neighbor
        nearest = None
        for neighbor, distance in graph[current].items():
            if neighbor not in visited and (nearest is None or distance < graph[current][nearest]):
                nearest = neighbor
        
        # Update path and cost
        if nearest is not None:
            path.append(nearest)
            cost += graph[current][nearest]
        else:
            # If no unvisited neighbors, return to starting node
            path.append(start)
            cost += graph[current][start]
    
    return (path, cost)

# Example usage
if __name__ == '__main__':
    # Create a sample graph
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 4},
        'C': {'A': 3, 'B': 4},
    }
    # Get starting node from command line
    start = sys.argv[1] if len(sys.argv) > 1 else 'A'
    # Solve the TSP
    path, cost = tsp(graph, start)
    # Print the result
    print(f'TSP path: {" -> ".join(path)}')
    print(f'TSP cost: {cost}')

