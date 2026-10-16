# MINI CODING PROJ - SMART TRAVEL PLANNER
# Use all three techniques from this chapter in one travel planner that:
# uses RECURSION to explore all travel routes between two cities
# uses DYNAMIC PROGRAMMING to calculate the minimum travel cost across checkpoints
# uses a GREEDY approach to pick the nearest next city

# ---------- RECURSION: explore all travel routes ----------
routes = {
    "Delhi": ["Jaipur", "Agra"],
    "Jaipur": ["Udaipur"],
    "Agra": ["Udaipur"],
    "Udaipur": [],
}

def find_routes(graph, start, end, path=None):
    path = (path or []) + [start]
    if start == end:
        return [path]
    else: 
        all_routes = []
    for city in graph[start]:
        all_routes += find_routes(graph, city, end, path)
    return all_routes

# ---------- DP: minimum travel cost across checkpoints ----------

def min_travel_cost(tolls):
    n = len(tolls)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        step1 = dp[i - 1] + tolls[i - 1]
        if i >= 2:
            step2 = dp[i - 2] + tolls[i - 1]
        else:
            step2 = step1
        dp[i] = min(step1, step2)
    return dp[n]

# ---------- GREEDY: always go to the nearest next city ----------

def nearest_city(distances, start):
    visited = [start]
    current = start
    while len(visited) < len(distances):
        options = {}
        for c,d in distances[current].items():
            if c not in visited:
                options[c] = d
        if not options:
            break
        nearest = min(options, key=options.get)
        visited.append(nearest)
        current = nearest
    return visited

# ---------- Run ----------
print(" All routes Delhi -> Udaipur:")
print()
for r in find_routes(routes, "Delhi", "Udaipur"):
    print("   " + " -> ".join(r))
print()

print("Min travel cost:", min_travel_cost([100, 50, 150, 50]))

distances = {
    "Delhi": {"Jaipur": 280,
              "Agra": 230},
    "Jaipur": {"Delhi": 280,
               "Agra": 240},
    "Agra": {"Delhi": 230,
             "Jaipur": 240},
}
print("Greedy nearest tour from Delhi:", nearest_city(distances, "Delhi"))