from primes import *

primesUpTo = 2000000 # 2M
pList = primes(primesUpTo)
pSet = set(pList)

def isPrime(n):
    if n < primesUpTo: return n in pSet
    if n > primesUpTo**2: raise Exception('increase prime cache')

    # check if there are any prime divisors up to sqrt(n)
    checkUpTo = int(n**0.5)+1
    for x in pList:
        if x > checkUpTo: return True      
        if n % x == 0: return False


# Takes ~ minute to run
sides = 4
n = 1
d = 2 # delta
count = 0
total = 1
while True:
    total += sides
    for i in range(sides):
        n = n + d
        if isPrime(n): count += 1    

    if float(count) / total < 0.1:
        print 'Answer (length): ' + str(d+1)
        break

    d += 2
    

