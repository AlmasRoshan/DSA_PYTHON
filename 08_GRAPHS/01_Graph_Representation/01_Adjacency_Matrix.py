# ADJACENCY MATRIX

# Delhi -- Mumbai
#   |          |
# Kolkata -- Chennai 

cities = ["Delhi","Mumbai","Kolkata","Chennai"]

matrix = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]

print("Delhi - Mumbai connected?", matrix[0][1] == 1)   # True
print("Delhi - chennai connected?", matrix[0][3] == 1)  # False

# List Comprehension
neighbour = [cities[j] for j in range(4) if matrix[0][j] == 1]
print("Delhi's neighbour:", neighbour)  # ["Mumbai", "Kolkata"]
