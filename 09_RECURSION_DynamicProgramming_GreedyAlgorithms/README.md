# Recursion, Dynamic Programming & Greedy Algorithms

---

## 1. Recursion

### What is Recursion?
Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem by breaking it down into smaller, self-similar subproblems.

### The Call Stack
* When a function is invoked, the computer allocates a **stack frame** on the **call stack**.
* Each frame holds local variables, parameters, and the return address where execution resumes after the function finishes.
* As recursive calls occur, frames are pushed onto the stack.
* When a base case is hit, values are returned and the stack frames are popped in Last-In, First-Out (**LIFO**) order.
* **Stack Overflow:** If recursion runs too deep without terminating, memory allocated for the call stack runs out. In Python, this triggers `RecursionError: maximum recursion depth exceeded`.

### Two Main Parts of a Recursive Function
1. **Base Case:** The condition that stops recursion and returns a direct value immediately.
2. **Recursive Case:** The line where the function calls itself with a modified, smaller input to progress toward the base case.

```python
def factorial(n):
    # 1. Base Case
    if n <= 1:
        return 1
    # 2. Recursive Case
    return n * factorial(n - 1)
```

### Recursion vs. Iteration

| Feature | Recursion | Iteration (`for` / `while`) |
| :--- | :--- | :--- |
| **Execution** | Function calls itself | Block of code repeats inside a loop |
| **State Storage** | Managed implicitly on the call stack | Managed explicitly via counters and pointers |
| **Memory** | Uses $O(n)$ stack memory | Typically uses $O(1)$ auxiliary memory |
| **Speed** | Slower due to frame push/pop overhead | Faster execution speed |
| **Best Used For** | Tree traversals, graphs, divide & conquer | Flat list traversals, simple counting |

---

## 2. Dynamic Programming (DP)

### What is Dynamic Programming?
Dynamic Programming is an optimization technique used on problems that have repeating subproblems. Instead of recomputing the same answers again and again, DP computes each subproblem once, saves the result, and reuses it.

### Two Necessary Properties for DP
1. **Optimal Substructure:** The optimal solution to the overall problem can be built using the optimal solutions of its smaller subproblems (written as a mathematical recurrence relation, like $F(n) = F(n-1) + F(n-2)$).
2. **Overlapping Subproblems:** The same sub-calculations appear multiple times across different branches of the problem tree.

---

### Memoization (Top-Down Approach)
* Starts from the top target ($n$) and breaks it down toward the base cases using recursion.
* Uses an external lookup table (like a Python dictionary `{}`) to cache computed results.
* **Mechanism:** Before calculating, check if the value is already in the dictionary. If yes, return it instantly; if not, calculate it, store it in the dictionary, and return it.

```python
def fib_memo(n, memo=None):
    # None check prevents Python's shared mutable default argument trap
    if memo is None:
        memo = {}
        
    # Base Case
    if n <= 1:
        return n
        
    # Check if already solved (Cache Hit)
    if n in memo:
        return memo[n]
        
    # Solve, save to memo, and return
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

---

### Tabulation (Bottom-Up Approach)
* Starts from the smallest base cases ($0, 1$) and iteratively builds up to $n$ using a loop.
* Allocates a list (table) of size `n + 1` filled with initial values (usually `0`).
* No recursion, no call stack buildup.

```python
def fib_table(n):
    if n <= 1:
        return n
        
    # Allocate table of size n + 1
    table = [0] * (n + 1)
    table[1] = 1  # Base case setup
    
    # Build up from index 2 to n
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
        
    return table[n]
```

---

### Memoization vs. Tabulation

| Parameter | Memoization (Top-Down) | Tabulation (Bottom-Up) |
| :--- | :--- | :--- |
| **Method** | Recursion + Cache (Dictionary) | Loops (`for`) + Table (List) |
| **Computation** | Solves only subproblems that are queried | Solves all subproblems systematically |
| **Stack Space** | Consumes $O(n)$ recursion stack space | Uses $O(1)$ stack space |
| **Space Optimization** | Difficult to optimize past $O(n)$ | Can often be reduced to $O(1)$ using 2 variables |
| **Stack Overflow Risk** | Yes, if $n$ exceeds recursion depth | Never overflows the call stack |

#### Which One to Use?
* **Use Tabulation:** When you need production-grade performance, want to avoid recursion depth errors, or can optimize space down to $O(1)$ by keeping only the last few calculated values.
* **Use Memoization:** When the problem space is huge and sparse (many states exist, but only a fraction are ever needed), or when recursive logic is much simpler to write first.

---

## 3. Greedy Algorithms

### What is a Greedy Algorithm?
A Greedy Algorithm solves a problem by making the **locally optimal choice** at every individual step, hoping that these local choices will add up to the global optimum.

* It never looks backward or reconsiders past decisions.
* It does not evaluate future consequences.
* It never backtracks.

---

### Example: Indian Currency Coin Change
Given an amount, pick the fewest notes/coins to make the total. We always greedily grab the highest value coin/note first.

Standard denominations: `[500, 200, 100, 50, 20, 10, 5, 2, 1]`

```python
def make_change(amount):
    coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = []
    
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
            
    return result

# Example:
# make_change(87) -> [50, 20, 10, 5, 2]
```

---

### Greedy vs. Dynamic Programming

Greedy algorithms run very fast ($O(n)$ or $O(n \log n)$), but **greedy does not work for every problem**.

#### Where Greedy Fails (Arbitrary Coin Systems)
* Standard currencies (like Indian Rupee or US Dollar) are designed as "canonical coin systems," where greedy is mathematically guaranteed to work.
* If arbitrary coins are used, greedy can produce suboptimal results:
  * **Coins available:** `[4, 3, 1]`
  * **Target amount:** `6`
  * **Greedy approach:** 
    1. Grabs `4` $\rightarrow$ remaining `2`.
    2. Grabs `1` $\rightarrow$ remaining `1`.
    3. Grabs `1` $\rightarrow$ remaining `0`.
    * Total coins: `[4, 1, 1]` = **3 coins**
  * **DP approach (Optimal):**
    * Tries combinations and finds `3 + 3 = 6`.
    * Total coins: `[3, 3]` = **2 coins**

### Summary Comparison

| Property | Greedy Algorithm | Dynamic Programming |
| :--- | :--- | :--- |
| **Approach** | Picks best local option right now | Explores and weighs subproblem paths |
| **Backtracking** | Never backtracks | Evaluates multiple paths to pick the true minimum/maximum |
| **Guarantee** | Only optimal if the greedy-choice property holds | Always guarantees optimal answer if formulated correctly |
| **Speed** | Very fast ($O(n)$ to $O(n \log n)$) | Slower, polynomial ($O(n^2)$, $O(n \cdot W)$, etc.) |
| **Code Simplicity** | Very simple loop and sort | Requires recurrence formula and DP table/cache |