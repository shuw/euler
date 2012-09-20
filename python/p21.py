from math import *

# Returns hash of prime factors + their power
def findPrimeFactors(n, factors):
    if n == 1:
        return;

    secondLargestPrimeFactor = int(sqrt(n))
    i = 2;
    while True:
        if i == n or  i > secondLargestPrimeFactor:
            power = factors.get(n)
            if power == None:
                factors[n] = 0
            factors[n] += 1            
            return
        
        if (n / float(i)) % 1 == 0:
            x = findPrimeFactors(i, factors)
            y = findPrimeFactors(n / i, factors)
            return
        i = i + 1

class PrimePart:
    def __init__(self, prime, power):
        self.prime = prime
        self.power = power
    def __repr__(self):
        return str(self.prime) + "^" + str(self.power)
    

def divisorsRecursive(primes, index, product, divisors):
    if index == len(primes):
        divisors.append(product)
        return

    divisorsRecursive(primes, index + 1, product, divisors)

    primePart = primes[index]
    for i in range(primePart.power):
        product = product * primePart.prime        
        divisorsRecursive(primes, index + 1, product, divisors)
    

def properDivisorsSum(n):
    factors = {}
    findPrimeFactors(n, factors)

    primes = []
    for i in factors:
        primes.append(PrimePart(i, factors[i]))

    divisors = []
    divisorsRecursive(primes, 0, 1, divisors)

    sum = 0
    for d in divisors: sum += d
    sum -= n # subtract the number itself because divisorsRecursive includes n as a divisor

    return sum       

amicableSum = 0
for n in range(2, 10000):
    dSum = properDivisorsSum(n)
    dSumSum = properDivisorsSum(dSum)

    isAmicable = dSumSum == n and n != dSum
    if isAmicable:
        amicableSum += n
        print str(n) + " -> " + str(dSum) + " -> " + str(dSumSum)
    
print "Answer " + str(amicableSum)
