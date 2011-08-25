import numpy
import math

def primes(upto):
    evenNumbers = numpy.arange(3,upto+1,2)

    primeMap = numpy.ones((upto-1)/2,dtype=bool)
    for factor in evenNumbers[:int(math.sqrt(upto))]:
        if primeMap[(factor-2)/2]:
                primeMap[(factor*3-2)/2::factor] = 0

    return numpy.insert(evenNumbers[primeMap], 0, 2)
            
primes = primes(10000000)
primeSet = set(primes)

def truncatedprimes(p):
    p2 = p
    pReversed = 0
    satisfied = True
    while True:
        pReversed = pReversed * 10 + p2 % 10
        p2 = p2 / 10
        print 'f' + str(p2) 
        print 'r' + str(pReversed)
        if p2 == 0:
            break
        if p2 not in primeSet or pReversed not in primeSet:
            satisfied = False
            break
    return satisfied

def answer():
    for p in primes:
        if p > 10:
            if truncatedprimes(p):
                print p


truncatedprimes(3797)
