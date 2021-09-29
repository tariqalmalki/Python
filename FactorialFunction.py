#6! ==> 6 x 5 x 4 x 3 x 2 x 1

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

for n in range(1, 10): # testing
    print(n, factorialFun(n))
