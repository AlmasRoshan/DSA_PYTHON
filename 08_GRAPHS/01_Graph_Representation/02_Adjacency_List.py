# ADJACENCY LIST

graph = {
    "Delhi":["Mumbai", "Kolkata"],
    "Mumbai":["Delhi", "Chennai"],
    "Kolkata":["Delhi", "Chennai"],
    "Chennai":["Mumbai", "Kolkata"]
}

print("Delhi's neighbour:", graph["Delhi"]) # ["Mumbai", "Kolkata"]
print("Is Delhi-Chennai a direct road?", "Chennai" in graph["Delhi"])   # False

# List every road once 
for city, road in graph.items():
    print(f"{city} -> {road}")
