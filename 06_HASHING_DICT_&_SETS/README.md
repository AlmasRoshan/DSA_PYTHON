# Hashing, Dictionaries, and Sets: Quick Revision Sheet

---

## 1. Core Hashing Concepts

* **Hashing:** Converting arbitrary data (key) into a fixed-size integer using a hash function.
* **Hash Table:** An array of buckets where data items are stored based on their hash value.
* **Hash Collision:** When two distinct keys produce the same hash index.
* **Collision Handling:**
  * **Separate Chaining:** Each bucket points to a linked list or array storing collided elements.
  * **Open Addressing:** Finds the next empty bucket slot (e.g., Linear Probing).

---

## 2. Python Dictionaries (`dict`)

Key-value mapping data structure with unique, hashable keys.

### Basic Operations (CRUD)

```python
# 1. Create
user = {"name": "Alice", "age": 25}

# 2. Insert & Update
user["role"] = "Admin"    # Insert a new key-value pair
user["age"] = 26          # Update an existing key

# 3. Access
print(user["name"])       # "Alice" (raises KeyError if key does not exist)
print(user.get("age"))    # 26 (returns None if key is absent; safe access)
print(user.get("city", "Unknown"))  # "Unknown" (custom default fallback)

# 4. Delete
del user["role"]              # Removes key; raises KeyError if not found
removed_age = user.pop("age") # Removes key and returns its value
```

### Essential Dictionary Methods

```python
d = {"a": 1, "b": 2}

d.keys()          # dict_keys(['a', 'b'])
d.values()        # dict_values([1, 2])
d.items()         # dict_items([('a', 1), ('b', 2)])
d_copy = d.copy() # Shallow copy of dictionary
d.clear()         # Empties the dictionary: {}
```

### Traversing a Dictionary

```python
data = {"x": 10, "y": 20}

# 1. Loop over keys (default behavior)
for key in data:
    print(key)

# 2. Loop over values
for val in data.values():
    print(val)

# 3. Loop over key-value pairs
for key, val in data.items():
    print(key, val)
```

---

## 3. Python Sets (`set`)

Unordered collections of unique, hashable elements.

### Creation and Element Operations

```python
# Create
s = {1, 2, 3}
empty_s = set()   # Note: {} creates an empty dict, not a set!

# Add element
s.add(4)          # {1, 2, 3, 4}

# Remove vs Discard
s.remove(2)       # Removes 2; raises KeyError if not found
s.discard(99)     # Removes 99; does NOTHING if not found (no error!)

# Pop and Clear
val = s.pop()     # Removes and returns an arbitrary element
s.clear()         # Clears all elements: set()
```

### Set Mathematical Operations

```python
A = {1, 2, 3}
B = {3, 4, 5}

A | B             # Union: {1, 2, 3, 4, 5}
A & B             # Intersection: {3}
A - B             # Difference (in A, not in B): {1, 2}
A ^ B             # Symmetric Difference (elements in either, not both): {1, 2, 4, 5}
```

---

## 4. Practical Problem Patterns

### 1. Frequency Counting

```python
# A. Character Frequency
text = "banana"
char_counts = {}
for ch in text:
    char_counts[ch] = char_counts.get(ch, 0) + 1
# Result: {'b': 1, 'a': 3, 'n': 2}

# B. Word Frequency in a Sentence
sentence = "apple banana apple orange"
word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1
# Result: {'apple': 2, 'banana': 1, 'orange': 1}

# C. Frequency of Items in a List
nums = [10, 20, 10, 30, 20]
num_counts = {}
for n in nums:
    num_counts[n] = num_counts.get(n, 0) + 1
# Result: {10: 2, 20: 2, 30: 1}
```

### 2. Detecting Duplicates

```python
nums = [1, 2, 3, 2, 4]

# Quick Check: Does the list contain any duplicates?
has_duplicates = len(nums) != len(set(nums))  # True

# Find the duplicate elements:
seen = set()
duplicates = set()

for item in nums:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(duplicates) # {2}
```

---

## 5. Time Complexity & Comparisons

### Big-O Time Complexity

| Data Structure | Lookup (`in`) | Insert | Delete | Why? |
| :--- | :--- | :--- | :--- | :--- |
| **`list`** | **$O(N)$** | $O(1)$ append / $O(N)$ insert | $O(N)$ | Linear search through contiguous memory. |
| **`dict`** | **$O(1)$** avg | $O(1)$ avg | $O(1)$ avg | Direct hash addressing of keys. |
| **`set`** | **$O(1)$** avg | $O(1)$ avg | $O(1)$ avg | Hash table structure without value storage. |

> **Note on Worst-Case:** `dict` and `set` can hit **$O(N)$** in worst-case scenarios when heavy hash collisions occur, but on average they operate in **$O(1)$** constant time.

### Summary: When to Use What?

* **Use `list`:** When order matters, duplicate elements are needed, or indexing (`arr[i]`) is required.
* **Use `set`:** When fast membership testing (`item in set`), removing duplicates, or mathematical set operations are needed.
* **Use `dict`:** When associating keys with values, tracking counts/frequencies, or looking up items by unique identifiers.
