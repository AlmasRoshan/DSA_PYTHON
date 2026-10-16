# DSA with Python: Arrays (Lists) & Strings Notes

---

## 1. Arrays (Lists in Python)

### What is an Array?
* An ordered collection of items stored in contiguous memory positions.
* In Python, dynamic arrays are implemented natively using the `list` data type.

### Creating an Array & Indexing
* **0-based indexing:** Elements start from index `0` up to `n - 1`.
* **Negative indexing:** Access elements from the end (`-1` is the last element).

> `arr = [10, 20, 30, 40]`  
> `first = arr[0]` # 10  
> `last = arr[-1]` # 40  

---

### Traversing Arrays

* **`for` loop:** Iterates directly over each element one by one.
> `for item in arr:`  
> &nbsp;&nbsp;&nbsp;&nbsp;`print(item)`

* **`while` loop:** Uses an explicit index tracker, condition, and increment/decrement. Provides full customization over step size and direction.
> `i = 0`  
> `while i < len(arr):`  
> &nbsp;&nbsp;&nbsp;&nbsp;`print(arr[i])`  
> &nbsp;&nbsp;&nbsp;&nbsp;`i += 1`

* **`enumerate()` function:** Built-in generator yielding `(index, value)` pairs automatically without manual counter incrementation.
> `for idx, val in enumerate(arr):`  
> &nbsp;&nbsp;&nbsp;&nbsp;`print(f"{idx}: {val}")`

---

### Array Operations & Big O Complexity

| Operation | Method / Syntax | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| **Access / Read** | `arr[i]` | Direct index lookup | O(1) |
| **Update** | `arr[i] = val` | Overwrites value at index | O(1) |
| **Append** | `arr.append(val)` | Adds element to the end | O(1) amortized |
| **Insert** | `arr.insert(i, val)` | Inserts at index; shifts remaining elements | O(n) |
| **Delete** | `del arr[i]` | Removes element by index; shifts items | O(n) |
| **Pop** | `arr.pop()` / `arr.pop(i)` | Removes last item (O(1)) or specific index (O(n)) | O(1) or O(n) |
| **Remove** | `arr.remove(val)` | Searches and removes first matching value | O(n) |
| **Clear** | `arr.clear()` | Empties the entire list | O(n) |
| **Search** | `val in arr` / `arr.index(val)` | Linear scan from left to right | O(n) |
| **Count** | `arr.count(val)` | Counts occurrences of value | O(n) |
| **Sort** | `arr.sort()` / `sorted(arr)` | Orders items using Timsort | O(n log n) |
| **Reverse** | `arr.reverse()` / `arr[::-1]` | Inverts list order | O(n) |

---

## 2. Strings

### What is a String?
* An ordered, immutable sequence of characters.
* Created using single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` / `"""..."""`) for multi-line strings and docstrings.
* **Formatted Strings (f-strings):** Python's equivalent to JavaScript template literals (backticks with `${}`), written using `f"..."` with curly braces `{}`.

> `single_quoted = 'DSA'`  
> `double_quoted = "Python"`  
> `f_string = f"Topic: {single_quoted} in {double_quoted}"`  

---

### String Indexing & Slicing
* Slicing follows the pattern `string[start:stop:step]` (stop index is exclusive).

> `text = "Python"`  
> `sub = text[0:4]` # "Pyth"  
> `rev = text[::-1]` # "nohtyP" (Reversed string)  

---

### Common String Operations

| Operation | Method / Syntax | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| **Length** | `len(s)` | Returns total number of characters | O(1) |
| **Case change** | `s.upper()` / `s.lower()` | Returns all-uppercase or all-lowercase copy | O(n) |
| **Replace** | `s.replace(old, new)` | Replaces occurrences of a substring | O(n) |
| **Find** | `s.find(sub)` | Returns starting index of substring (or -1) | O(n) |
| **Count** | `s.count(sub)` | Counts non-overlapping occurrences | O(n) |
| **Strip** | `s.strip()` | Removes leading and trailing whitespace | O(n) |
| **Split** | `s.split(sep)` | Splits string into a list of words by delimiter | O(n) |
| **Join** | `sep.join(list_of_str)` | Combines a list of strings into one string | O(n) |
| **Starts with** | `s.startswith(prefix)` | Checks if string begins with prefix | O(k) (k = len(prefix)) |
| **Ends with** | `s.endswith(suffix)` | Checks if string ends with suffix | O(k) (k = len(suffix)) |

---

## 3. Mutability: List vs. String

* **Lists are Mutable:** Can be modified, appended, or sorted in-place without altering the original memory reference.
> `nums = [1, 2, 3]`  
> `nums[0] = 99` # Valid: nums becomes [99, 2, 3]  

* **Strings are Immutable:** Characters cannot be updated in-place. Any modification creates a brand-new string in memory.
> `word = "hello"`  
> `# word[0] = "H" raises TypeError`  
> `word = "H" + word[1:]` # Creates a new string "Hello"