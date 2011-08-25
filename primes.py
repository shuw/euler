import numpy
import math

def primes(upto):
    evenNumbers = numpy.arange(3,upto+1,2)

    primeMap = numpy.ones((upto-1)/2,dtype=bool)
    for factor in evenNumbers[:int(math.sqrt(upto))]:
        if primeMap[(factor-2)/2]:
                primeMap[(factor*3-2)/2::factor] = 0

    return numpy.insert(evenNumbers[primeMap], 0, 2)
