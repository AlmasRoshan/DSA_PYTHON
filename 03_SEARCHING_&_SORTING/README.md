# Searching and Sorting Quick Reference Guide

---

## 1. Searching Algorithms

Searching is the process of locating a specific element within a collection of data.

| Algorithm | How It Works | Requirement | Time Complexity (Best / Worst) | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | Checks each element one by one from start to end until a match is found. | None (works on unsorted & sorted data). | O(1) / O(n) | O(1) |
| **Binary Search** | Repeatedly divides the search interval in half by comparing the target to the middle element. | **Must be sorted**. | O(1) / O(log n) | O(1) iterative, O(log n) recursive |

* **Key Difference:** Linear search is flexible but slow (O(n)) for large data; binary search is much faster (O(log n)) but strictly requires pre-sorted data.

---

## 2. Sorting Algorithms

Sorting arranges data in a specific order (ascending or descending).

| Algorithm | Core Mechanism | Time (Best / Avg / Worst) | Space Complexity | Stable? |
| :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | Repeatedly compares adjacent neighbors and swaps them if out of order. | O(n) / O(n²) / O(n²) | O(1) | Yes |
| **Selection Sort** | Scans unsorted elements to select the absolute minimum and places it into index i. | O(n²) / O(n²) / O(n²) | O(1) | No |
| **Insertion Sort** | Shifts larger elements to the right and inserts the current key into its correct slot. | O(n) / O(n²) / O(n²) | O(1) | Yes |
| **Merge Sort** | Recursively cuts list in half, then merges sorted halves back together. | O(n log n) across all cases | O(n) | Yes |
| **Quick Sort** | Picks a pivot, partitions elements around it, and recursively sorts subarrays. | O(n log n) / O(n log n) / O(n²) | O(log n) auxiliary | No |

---

## 3. Which Algorithm to Choose?

* **Use Insertion Sort:** For small lists (n < 50) or data that is already almost sorted (runs in O(n) time).
* **Use Merge Sort:** When guaranteed O(n log n) performance and stability are mandatory, and extra memory (O(n)) is available.
* **Use Quick Sort:** When in-place sorting and fast average runtime are needed without allocating extra array copies.
* **Avoid in Production:** Bubble Sort and Selection Sort, due to poor O(n²) scalability.

---

## 4. Real-World Programming vs. Manual Sorting

In production, developers do not write custom sorting algorithms from scratch; they use language built-ins:

* **`list.sort()`:** Sorts the list **in-place** (modifies original list) and returns `None`.
* **`sorted(iterable)`:** Leaves the original list intact and returns a **new sorted list**.
* **Parameters:** Both support `reverse=True` for descending order and `key=` (e.g., `key=str.lower` for case-insensitive sorting).
* **Under the Hood:** Python uses **Timsort** (a hybrid of Merge Sort and Insertion Sort) running in O(n log n) time, heavily optimized in C.

> **Why learn them manually?**  
> Implementing these algorithms develops pointer manipulation, recursion, loop invariant tracking, and complexity analysis—foundational skills essential for algorithm design and technical interviews.