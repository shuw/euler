import copy
import math
import numpy


def findPrimes(upto):
    evenNumbers = numpy.arange(3,upto+1,2)

    primeMap = numpy.ones((upto-1)/2,dtype=bool)
    for factor in evenNumbers[:int(math.sqrt(upto))]:
        if primeMap[(factor-2)/2]:
                primeMap[(factor*3-2)/2::factor] = 0

    return numpy.insert(evenNumbers[primeMap], 0, 2)

primes = findPrimes(1000000)
primesSet = set(primes)


def isCircular(n):
    digits = str(n)
    numDigits = len(digits)
    for i in range(numDigits):
        circ = ''
        for j in range(numDigits):
            circ += digits[(j + i) % numDigits]

        if int(circ) not in primesSet:
            return False

    return True        

def findCircularPrimes():
    circularPrimes = 0
    for c in (p for p in primes if isCircular(p)):
        circularPrimes += 1
        print c
    return circularPrimes

print 'Answer: ' + str(findCircularPrimes())
