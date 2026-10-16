# BREADTH FIRST SEARCH (BFS)
# follows queue (FIFO)
# explore level-by-level

from collections import deque

graph = {
    "Delhi":["Mumbai", "Kolkata"],
    "Mumbai":["Delhi", "Bengaluru"],
    "Kolkata":["Delhi", "Chennai"],
    "Chennai":["Kolkata", "Bengaluru"],
    "Bengaluru":["Mumbai", "Chennai"]
}

def bfs(graph, start):
    visited = set([start])  # track visited, the visited vertex will add into this set()
    queue = deque([start])  
    order = [] 
    while queue:
        city = queue.popleft()
        order.append(city)
        for neighbour in graph[city]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return order
print(bfs(graph, "Delhi"))