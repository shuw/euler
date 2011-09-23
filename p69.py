from primes import *

pSet = set(primes(1000000))


def countRelativelyPrimeFactors

pCount = 0
maxResult = 0
answer = 0
for n in range(1, 1000001):
    result = float(n) / pCount if pCount != 0 else 0
        
    if result > maxResult:
        answer = n
        # print 'value: ' + str(result) + ' n: ' + str(n)
        maxResult = result

    if n in pSet: pCount += 1

print answer
