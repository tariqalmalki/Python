##x = int(input("Please enter the number for formula n! = "))
##
##def exclamationFormula(x):
##    if x == 0:
##        print(f'{x}! --> {x}')
##    totals = 1
##    for i in range(1,x +1):
##        totals *= i
##        print(f'{i}! --> {totals}')
##exclamationFormula(x)
    
    

##def factorialFun(n):
##    if n < 0:
##        return None
##    if n < 2:
##        return 1
##    
##    product = 1
##    for i in range(2, n + 1):
##        product *= i
##    return product
##
##for n in range(1, 10): # testing
##    print(n, factorialFun(n))

#6! ==> 6 x 5 x 4 x 3 x 2 x 1

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

for n in range(1, 10): # testing
    print(n, factorialFun(n))
