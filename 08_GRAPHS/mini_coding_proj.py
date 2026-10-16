# MINI CODING PROJ - CITY ROUTE EXPLORER
# Build a graph of Indian cities and explore it. Your program should:
# create a GRAPH OF CITIES connected by roads(adjacency list)
# DISPLAY the graph
# find ALL REACHABLE CITIES from a start using BFS
# EXPLORE ROUTES using DFS
# BONUS: check whether two cities are CONNECTED.

from collections import deque

class CityGraph:
    def __init__(self):
        self.roads = {}

    # add cities
    def add_city(self, city):
        self.roads.setdefault(city, [])

    # add roads
    def add_road(self, city1, city2):
        self.roads.setdefault(city1, []).append(city2)
        self.roads.setdefault(city2, []).append(city1)

    def display(self):
        for city, links in self.roads.items():
            print(f"    {city} -> {links}")

    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        order = []
        while queue:
            city = queue.popleft()
            order.append(city)
            for neighbour in self.roads[city]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return order

    def dfs(self, start, visited=None, order=None):
        if visited is None:
            visited = set()
            order = []

        visited.add(start)
        order.append(start)
        for neighbour in self.roads[start]:
            if neighbour not in visited:
                self.dfs(neighbour, visited, order)
        return order

    # checks whether 2 cities are conneted, 
    # returns True if path exists btw city1 & city2 else returns False
    def is_connected(self, city1, city2):
        return city2 in self.bfs(city1)

graph = CityGraph()
roads = [
    ("Delhi", "Mumbai"),
    ("Delhi", "Kolkata"),
    ("Mumbai", "Banglore"),
    ("Kolkata", "Chennai"),
    ("Chennai","Banglore")
]

for a,b in roads:
    graph.add_road(a, b)

print("City Map:")
print()
graph.display()
print()

print("Reachable from Delhi(BFS):", graph.bfs("Delhi"))
print("Route explore from Delhi(DFS):", graph.dfs("Delhi"))
print("Is Delhi connected to Chennai?", graph.is_connected("Delhi", "Chennai"))
