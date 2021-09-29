from math import e, exp, log
# e → a constant with a value that is an approximation of Euler's number (e)
# exp(x) finding the value of e ** x;
# log(x) → the natural logarithm of x
# log(x, b) → the logarithm of x to base b
# log10(x) → the decimal logarithm of x (more precise than log(x, 10))
# log2(x) → the binary logarithm of x (more precise than log(x, 2))
# pow(x, y) → finding the value of x ** y (mind the domains)
print("e = ",e)
print("exp(0) = ",exp(0))
print("exp(e) = ",exp(e))
print("log(e) = ",log(e))
print("log(2) = ",log(2))
print("log(e , e) = ",log(e , e))
print("log(8,2) = ",log(8,2))
print("pow(e, 1) == exp(log(e)) = ",pow(e, 1) == exp(log(e)))
print("pow(2, 2) == exp(2 * log(2)) = ",pow(2, 2) == exp(2 * log(2)))
print("log(e, e) == exp(0) = ",log(e, e) == exp(0))
