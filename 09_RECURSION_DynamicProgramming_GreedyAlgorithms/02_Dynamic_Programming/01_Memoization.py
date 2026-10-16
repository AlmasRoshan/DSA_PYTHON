# MEMOIZATION (TOP - BOTTOM)

def fib_memo(n, memo=None):
    if memo is None:
        memo = {}   # dict, which stores the ans that we've already computed
    if n <= 1:
        return n
    if n in memo:
        return memo[n]  # if the n is already stored in the dict, then return the ans of it
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo) # if not stored then compute it, using formula
    return memo[n]
print(fib_memo(6))
print(fib_memo(30))