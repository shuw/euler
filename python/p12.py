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


def numOfFactors(n):
    factors = {}
    findPrimeFactors(n, factors)
    
    product = 1
    for f1 in factors:
        # number of ways to choose from this factor is the count of this factor + the option not to select it
        choose = factors[f1] + 1
        product *= choose
    return product
    
def triangleNumber(n):
    return (n*n + n) / 2



found = False
n = 1
while not found:
    tNum = triangleNumber(n)
    factors = numOfFactors(tNum)

    print str(tNum) + " # factors: " + str(factors)
    if (factors > 500):
        found = True
    
    n += 1
