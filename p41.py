from math import *
from primes import *
import copy

pSet = set(primes(10000000))

# 9 & 8 can be excluded from search space because
# the sum of digits to 9 and to 8 are multiples of 9 which means the base 10 number
# they form are also divisible by 9
digits = [7,6,5,4,3,2,1]

def findPandigitalPrimes(available, path):
    if len(available) == 0:
        n = 0
        for d in path: n = d + n * 10

        if n in pSet:
            return n
        return None            
    
    for d in available:
        a2 = copy.copy(available)
        a2.remove(d)
        
        path.append(d)
        n = findPandigitalPrimes(a2, path)
        if n != None: return n
        path.pop()

print 'Answer: ' + str(findPandigitalPrimes(digits,[]))
