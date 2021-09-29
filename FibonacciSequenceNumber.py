#Fibonacci sequence, such that each number is the sum of the two preceding ones

def fib(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(0, 10): # testing
    print(n, "->", fib(n))
