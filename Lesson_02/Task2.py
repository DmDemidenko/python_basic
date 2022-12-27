# the second task to find the radius
import math
from math import pi
print('Please enter circle radius in (mm) :')
#input radius
r = (input())
#replace "," to "." to avoid errors
r = r.replace(",",".")
#change type of data to calculate result
r = float(r)
s = r * pi
print(f'Сircuit is {s} (mm)')
