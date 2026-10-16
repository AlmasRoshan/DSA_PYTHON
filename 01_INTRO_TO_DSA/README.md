# Chapter 1 — DSA Basics

## 1. What is Data?
Data is information that can be stored and processed by a computer (raw, unorgainsed).

> **Examples**
> ```python
> "John"
> 20
> [80, 75, 90]
> ```

## 2. What is a Data Structure?
A Data Structure is a way of storing and organizing data.

> **Examples**
> - List
> - Tuple
> - Stack
> - Queue
> - Tree
> - Graph
> - Dictionary

## 3. What is an Algorithm?
An Algorithm is a step-by-step method to solve a problem.

> **Example: Find the largest number**
> 1. Take the first number.
> 2. Compare it with the next number.
> 3. Keep the larger number.
> 4. Repeat until the end.

## 4. What is DSA?
DSA = Data Structures + Algorithms

*   **Data Structure:** How we store and organize data.
*   **Algorithm:** How we solve a problem.

DSA helps us solve problems efficiently.

## 5. Why Learn DSA?
*   To solve problems efficiently
*   To write better programs
*   To understand how data is stored
*   To choose the right approach for a problem
*   To prepare for coding interviews

## 6. Programming vs DSA
**Programming:** Writing code to solve a problem.

**DSA:** Choosing the right data structure and algorithm to solve the problem efficiently.

> Programming → Write the solution  
> DSA → Choose an efficient solution

## 7. Time Complexity
Time Complexity tells us how the running time of an algorithm grows as the input size increases.

| Complexity | Meaning |
| :--- | :--- |
| **O(1)** | Constant |
| **O(log n)** | Logarithmic |
| **O(n)** | Linear |
| **O(n log n)** | Linearithmic |
| **O(n²)** | Quadratic |

> **Examples**
> 
> **O(1)**
> ```python
> print(arr[0])
> ```
> 
> **O(n)**
> ```python
> for item in arr:
>     print(item)
> ```
> 
> **O(n²)**
> ```python
> for i in arr:
>     for j in arr:
>         print(i, j)
> ```

## 8. Space Complexity
Space Complexity tells us how much memory an algorithm uses as the input size increases.

| Complexity | Meaning |
| :--- | :--- |
| **O(1)** | Constant space |
| **O(n)** | Linear space |
| **O(n)** | Recursive calls |
| **O(n²)** | Quadratic space |

> **Note:** Recursive calls can use **O(n)** space when there are *n* calls on the call stack.

## 9. Big O Notation
Big O notation describes the growth of an algorithm's time or space complexity.

> **Rule 1 — Ignore Constants**
> - O(2n) → O(n)
> - O(5n) → O(n)
> - O(100n) → O(n)
> 
> *Constants are ignored.*

> **Rule 2 — Keep the Biggest Term**
> - O(n² + n) → O(n²)
> - O(n + log n) → O(n)
> - O(n³ + n² + n) → O(n³)
> 
> *Keep only the term that grows the fastest.*

---

## 10. Chapter 1 Summary

Data ->
Data Structure ->
Algorithm ->
DSA ->
Time & Space Complexity ->
Big O Notation

**Completed**
- [x] Data
- [x] Data Structures
- [x] Algorithms
- [x] DSA
- [x] Why Learn DSA
- [x] Programming vs DSA
- [x] Time Complexity
- [x] Space Complexity
- [x] Big O Notation
- [x] Big O Rules
- [X] Mini Coding Challenge