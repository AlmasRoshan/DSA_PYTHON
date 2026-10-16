# Graphs:

---

## 1. Introduction to Graphs

### What is a Graph?
A **Graph** is a non-linear data structure consisting of a finite set of vertices (or nodes) and a set of edges connecting these vertices.

* **Vertices ($V$):** The fundamental units or data points (e.g., cities, people, web pages).
* **Edges ($E$):** The connections or links joining pairs of vertices.

$$\text{Graph } G = (V, E)$$

---

## 2. Why Do We Need Graphs?
Linear data structures (Arrays, Linked Lists, Stacks, Queues) and hierarchical structures (Trees) cannot model **many-to-many relationships** or systems containing **cycles**:
* **Social Networks:** Connections where users follow or befriend each other mutually or unilaterally.
* **Navigation & Maps:** Road and metro networks where multiple intersections loop and intersect.
* **Routing Algorithms:** Finding optimal network packet delivery routes across the internet.
* **Dependency Resolution:** Package managers (`npm`, `pip`) resolving package dependencies.

---

## 3. Types of Graphs

### 3.1 Undirected Graph
Edges have no direction. The connection between two vertices is bidirectional ($A - B$ implies access from $A$ to $B$ and $B$ to $A$).

```text
A --- B
|     |
C --- D
```
* **Edges:** $(A, B), (A, C), (B, D), (C, D)$
* **Real-world Example:** Facebook friendship or mutual connection.

### 3.2 Directed Graph (Digraph)
Edges have a defined direction indicated by an arrow ($A \rightarrow B$ allows movement strictly from $A$ to $B$).

```text
A ---> B
^      |
|      v
C <--- D
```
* **Edges:** $(A \rightarrow B), (B \rightarrow D), (D \rightarrow C), (C \rightarrow A)$
* **Real-world Example:** Twitter/Instagram followers or web hyperlinks.

### 3.3 Unweighted Graph
All edges are treated equally. No numerical value or cost is associated with traveling across an edge.

```text
A --- B
|     |
C --- D
```
* **Real-world Example:** Basic connection status (e.g., whether two computers are plugged into the same local switch).

### 3.4 Weighted Graph
Each edge carries a numeric weight representing cost, distance, latency, or capacity.

```text
       5
  A ------- B
  |         |
2 |         | 8
  |         |
  C ------- D
       3
```
* **Edges:** $(A, B, 5), (A, C, 2), (C, D, 3), (B, D, 8)$
* **Real-world Example:** Flight paths where weight represents ticket price or travel duration.

### 3.5 Cyclic Graph
A graph containing at least one cycle (a path starting and ending at the same vertex without repeating edges).

```text
A ---> B
^      |
|      v
D <--- C
```
* **Cycle:** $A \rightarrow B \rightarrow C \rightarrow D \rightarrow A$
* **Real-world Example:** A circular rail loop or metro line.

### 3.6 Acyclic Graph
A graph that contains **no cycles**. It is impossible to start at any node and loop back to the same node along directed paths.

```text
A ---> B ---> D
|
v
C
```
* **Real-world Example:** A family tree, course prerequisites, or a Directed Acyclic Graph (DAG) used in task build systems.

---

## 4. Graph Representations

### 4.1 Adjacency Matrix
A 2D array of size $V \times V$ where rows represent the source node and columns represent the destination node.
* `matrix[i][j] = 1`: Edge exists between $i$ and $j$.
* `matrix[i][j] = 0`: No direct connection exists.

```python
# Mapping city names to row/column indices
# Delhi=0, Mumbai=1, Kolkata=2, Chennai=3
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai"]

# 1 indicates connected, 0 indicates not connected
matrix = [
    [0, 1, 1, 0],  # Row 0: Delhi connects to Mumbai(1) and Kolkata(2)
    [1, 0, 0, 1],  # Row 1: Mumbai connects to Delhi(0) and Chennai(3)
    [1, 0, 0, 1],  # Row 2: Kolkata connects to Delhi(0) and Chennai(3)
    [0, 1, 1, 0]   # Row 3: Chennai connects to Mumbai(1) and Kolkata(2)
]

# 1. Edge existence check in O(1) time
print("Delhi-Mumbai connected?", matrix[0][1] == 1)   # True
print("Delhi-Chennai connected?", matrix[0][3] == 1)  # False

# 2. Extracting neighbours using list comprehension
# Note: Use square brackets [] for a list comprehension, not ()
delhi_neighbours = [cities[j] for j in range(len(cities)) if matrix[0][j] == 1]
print("Delhi's neighbours:", delhi_neighbours)  # ['Mumbai', 'Kolkata']
```

### 4.2 Adjacency List
A hash map (dictionary) or array of lists where each vertex maps directly to a collection of its immediate neighbors.

```python
# Adjacency List representation using a Python dictionary
graph = {
    "Delhi": ["Mumbai", "Kolkata"],
    "Mumbai": ["Delhi", "Chennai"],
    "Kolkata": ["Delhi", "Chennai"],
    "Chennai": ["Mumbai", "Kolkata"]
}

# 1. Accessing neighbours directly in O(1) lookup
print("Delhi's neighbours:", graph["Delhi"])  # ['Mumbai', 'Kolkata']

# 2. Checking if an edge exists
print("Is Delhi connected to Mumbai?", "Mumbai" in graph["Delhi"])  # True
```

---

## 5. Adjacency Matrix vs. Adjacency List (Real-World Choice)

In software development and competitive programming, **Adjacency Lists are preferred in >90% of use cases**.

### Why Adjacency List Dominates:
1. **Sparsity:** Most practical graphs are **sparse** ($E \ll V^2$). For a network of 1,000,000 users where each user has 200 friends:
   * **Matrix:** Needs a $10^6 \times 10^6$ table ($10^{12}$ cells $\approx 1\text{ TB}$ RAM), almost entirely wasted on storing `0`s.
   * **List:** Stores only $10^6$ nodes and their actual connections ($O(V + E)$ space).
2. **Neighbour Iteration:** Finding all neighbors of node $u$ takes $O(\text{degree}(u))$ in a list versus $O(V)$ in a matrix (which requires iterating over the entire row).

### Complexity Comparison

| Operation | Adjacency Matrix | Adjacency List (Industry Standard) |
| :--- | :--- | :--- |
| **Space Complexity** | $O(V^2)$ | **$O(V + E)$** |
| **Check Edge $(u, v)$** | **$O(1)$** | $O(\text{degree}(u))$ |
| **Find All Neighbours of $u$** | $O(V)$ | **$O(\text{degree}(u))$** |
| **Add a Vertex** | $O(V^2)$ (resize matrix) | **$O(1)$** |
| **Add an Edge** | **$O(1)$** | **$O(1)$** |
| **Ideal Scenario** | Dense graphs ($E \approx V^2$), small $V \le 1000$ | Sparse graphs, real-world systems, maps, social networks |

---

## 6. Graph Traversals: BFS vs. DFS

```text
Sample Graph:
       ( A )
      /     \
    ( B )   ( C )
      \     /
       ( D )
```

### 6.1 Breadth-First Search (BFS)
* **Principle:** Explores nodes **level by level** (radially outward).
* **Data Structure:** **Queue** (First-In, First-Out / FIFO).
* **Key Guarantee:** Guarantees the **shortest path** (least number of edges) on an unweighted graph.

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])  # Tracks visited vertices to prevent infinite cycles
    queue = deque([start])  # Queue holds nodes pending expansion
    order = []

    while queue:
        city = queue.popleft()  # FIFO: Remove from front
        order.append(city)

        for neighbour in graph[city]:
            if neighbour not in visited:
                visited.add(neighbour)      # Mark visited immediately when queued
                queue.append(neighbour)     # Push to back of queue

    return order

# Example Graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print("BFS Order:", bfs(graph, "A"))
# Output: ['A', 'B', 'C', 'D']
```

#### BFS Traversal Tree
```text
           [ A ]           <--- Level 0
          /     \
       [ B ]   [ C ]       <--- Level 1
         |
       [ D ]               <--- Level 2
```

---

### 6.2 Depth-First Search (DFS)
* **Principle:** Explores **branch by branch**; dives as deep as possible down a path until a dead end is reached, then backtracks.
* **Data Structure:** **Stack** (Last-In, First-Out / LIFO) or **Call Stack (Recursion)**.
* **Primary Applications:** Cycle detection, topological sorting, pathfinding in mazes, connected components.

```python
def dfs(graph, start, visited=None, order=None):
    # Initialize visited and order on the very first function call
    if visited is None:
        visited = set()
        order = []

    # Mark current vertex
    visited.add(start)
    order.append(start)

    # Dive deeper into unvisited neighbours
    for neighbour in graph[start]:
        if neighbour not in visited:  # Crucial guard to avoid RecursionError
            dfs(graph, neighbour, visited, order)

    return order

# Example Graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print("DFS Order:", dfs(graph, "A"))
# Output: ['A', 'B', 'D', 'C']
```

#### DFS Traversal Tree
```text
       [ A ]
         |
       [ B ]               <--- Dive to first unvisited neighbour
         |
       [ D ]               <--- Dive to B's unvisited neighbour
         |
       [ C ]               <--- Dive to D's unvisited neighbour
```

---

### 6.3 Traversal Comparison Table

| Attribute | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| :--- | :--- | :--- |
| **Exploration Style** | Wide / Level by level | Deep / Branch by branch |
| **Underlying Structure** | Queue (FIFO via `collections.deque`) | Stack (LIFO via Recursion or list) |
| **Shortest Path (Unweighted)**| **Yes** (guaranteed) | No |
| **Memory Consumption** | $O(V)$ (stores current breadth frontier) | $O(\text{height})$ (stores recursion stack) |
| **Backtracking Needed?** | No | Yes (unwinds recursion upon dead ends) |
| **Primary Use Cases** | Shortest path, peer-to-peer networks, web crawlers | Solving mazes, cycle detection, topological sorting |

---

## 7. Shortest Path Concepts

1. **Unweighted Graph:**
   * Shortest path = path with the **minimum number of edges / hops**.
   * Solved using **BFS** in $O(V + E)$ time complexity.
2. **Weighted Graph:**
   * Shortest path = path with the **minimum sum of edge weights** (not necessarily fewest hops).
   * Solved using **Dijkstra's Algorithm** (for non-negative weights) or **Bellman-Ford Algorithm** (supports negative edge weights).