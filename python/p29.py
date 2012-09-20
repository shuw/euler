from math import *

found = {}

for a in range(2, 101):
  for b in range(2, 101):
    x = a**b
    found[x] = True

print(len(found))
