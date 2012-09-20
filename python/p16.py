from math import *

n = 1
for i in range(1000):
 n *= 2

sum = 0
for d in str(n):
  sum += int(d)

print(sum)
