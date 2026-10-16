# RECURSION

def  countdown(n):
    # base case (stop here)
    if n <= 0:
        return
    # recursive case (smaller problem)
    else:
        print(n)
        countdown(n - 1)
countdown(4)