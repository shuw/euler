import numpy
import math

def primes(upto):
    evenNumbers = numpy.arange(3,upto+1,2)

    primeMap = numpy.ones((upto-1)/2,dtype=bool)
    for factor in evenNumbers[:int(math.sqrt(upto))]:
        if primeMap[(factor-2)/2]:
                primeMap[(factor*3-2)/2::factor] = 0

    return numpy.insert(evenNumbers[primeMap], 0, 2)
            
primes = primes(1000000)
primeSet = set(primes)

def areLeftRightTruncationsPrimes(p):
    p2 = p
    pReversed = 0
    satisfied = True
    powerOfTen = 1
    while True:
        pReversed += (p2 % 10) * powerOfTen
        p2 = int(p2 / 10)
        powerOfTen *= 10
        if p2 == 0:
            break
        if p2 not in primeSet or pReversed not in primeSet:
            satisfied = False
            break
    return satisfied

def answer():
    sum = 0
    for p in primes:
        if p > 10:
            if areLeftRightTruncationsPrimes(p):
                sum += p
                print p
    return sum

print 'answer: ' + str(answer())
