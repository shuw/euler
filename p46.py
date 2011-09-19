from primes import *


pList = primes(10000)
pSet = set(pList)

def test(n):
    for p in pList:
        if p > n: break;
        if ((n-p) / 2) ** 0.5 % 1 == 0: return True
    return False

n = 1
while True:
    n += 2
    if n in pSet: continue
    if test(n) is False: break

print 'Answer: ' + str(n)
