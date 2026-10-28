graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []

    visited.add(start)
    order.append(start)
    for neigh in graph[start]:
        if neigh not in visited:
            dfs(graph, neigh, visited,order)
    return order 
print(dfs(graph, "A"))
