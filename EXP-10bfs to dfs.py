graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
# BFS implementation
def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)
            queue.extend(graph[node] - visited)

# DFS implementation
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
        

print("BFS traversal:")
bfs(graph, 'A')

print("\nDFS traversal:")
dfs(graph, 'A')
