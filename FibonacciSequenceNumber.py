##def fib(n):
##    
##    if n == 0:
##         return 0
##    if n < 3:
##        return 1
##
##    elem1 = elem2 = 1
##    sum = 0
##    for i in range(3, n + 1):
##        sum = elem1 + elem2
##        elem1, elem2 = elem2, sum
##    return sum
##
##
##for n in range(0, 10): # testing
##    print(n, "->", fib(n))

#Fibonacci sequence, such that each number is the sum of the two preceding ones

def fib(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(0, 10): # testing
    print(n, "->", fib(n))
