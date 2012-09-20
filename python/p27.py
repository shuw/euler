import math
import numpy


def primes(upto):
    evenNumbers = numpy.arange(3,upto+1,2)

    primeMap = numpy.ones((upto-1)/2,dtype=bool)
    for factor in evenNumbers[:int(math.sqrt(upto))]:
        if primeMap[(factor-2)/2]:
                primeMap[(factor*3-2)/2::factor] = 0

    return numpy.insert(evenNumbers[primeMap], 0, 2)

maxPrime = 1000000

p = primes(maxPrime)
pMap = {}
for n in p:
    pMap[n] = True


def getNumberOfPrimes(a, b):
    n = 0
    while True:        
        x = n*n + a*n + b
        if x > maxPrime:
            raise NameError("Need to raise prime number map ceiling. Trying to lookup: " + str(x))
        if pMap.get(x) == None:
            break
        n += 1
    return n

maxFactors = 0
for a in range(-1000,1000):
    for b in range(-1000, 1000):
        factors = getNumberOfPrimes(a, b)
        if factors > maxFactors:
            maxFactors = factors
            print "a =" + str(a) + " b=" + str(b) + " factors: " + str(factors)

        
    
