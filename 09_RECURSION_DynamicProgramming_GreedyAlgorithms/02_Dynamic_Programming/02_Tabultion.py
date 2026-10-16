# TABULATION (BOTTOM - TOP)
# TABULATION = table + loop
# f(n) = f(n-1) + f(n-2)

def fib_table(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
print(fib_table(6))
print(fib_table(10))