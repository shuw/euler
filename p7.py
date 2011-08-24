from math import *

n = 2

primesFound = 0
knownPrimes = [2]
while True:
    prime = True

    secondLargestPrimeFactor = int(sqrt(n))
    for i in knownPrimes:
        if i > secondLargestPrimeFactor:
            break;
        if (n / float(i)) % 1 == 0:
            prime = False
            break

    if prime:
        knownPrimes.append(n)
        if (primesFound % 100) == 0:
            print 'primes found: ' + str(primesFound)
        primesFound = primesFound + 1

    if prime and primesFound == 10001:
        print "FOUND: " + str(n)
        break
        

    n = n + 1

