# DEAPTH FISRT SEARCH
# follows stack (LIFO)
# starts from the root to the left child and then go deep until it reaches the leaf node then again checks its sibling(RIGHT)

graph = {
    "Delhi":["Mumbai", "Kolkata"],
    "Mumbai":["Delhi", "Bengaluru"],
    "Kolkata":["Delhi", "Chennai"],
    "Chennai":["Kolkata", "Bengaluru"],
    "Bengaluru":["Mumbai", "Chennai"]
}

def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []

    visited.add(start)
    order.append(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)   # dive deep
    return order
print(dfs(graph, "Delhi"))