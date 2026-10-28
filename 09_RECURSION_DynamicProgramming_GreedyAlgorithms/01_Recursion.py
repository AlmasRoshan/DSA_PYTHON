# RECURSION
# a fun which calls itself to solve the smaller version of the same problem 
# base case: a condition to stop
# first write base case then recursive case

def  countdown(n):
    # base case (stop here)
    if n <= 0:
        return
    # recursive case (smaller problem)
    else:
        print(n)
        countdown(n - 1)
countdown(4)