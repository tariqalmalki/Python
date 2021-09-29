from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad) # a function that converts x from degrees to radians;
ad = degrees(ar) # acting in the other direction (from radians to degrees)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
