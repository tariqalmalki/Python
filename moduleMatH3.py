from math import ceil, floor, trunc , factorial , hypot

# ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)

# floor(x) → the floor of x (the largest integer less than or equal to x)

# trunc(x) → the value of x truncated to an integer (be careful - it's
# not an equivalent either of ceil or floor)

# factorial(x) → returns x! (x has to be an integral and not a negative)

# hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle
# with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2))
# but more precise)


x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

print(factorial(5))
print(hypot(3 , 4))
