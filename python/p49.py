from primes import *
from digits import *

pList = primes(10000) # need up to 4 digits
pSet = set(pList)

for i in range(len(pList)):
    p = pList[i]    
    if p < 1000: continue

    for j in range(i+1, len(pList)):
        p2 = pList[j]
        p3 = (p2 - p) + p2
        if (p2 - p) + p2 in pSet:
            if set(toList(p)) == set(toList(p2)) == set(toList(p3)):
                print (p, p2, p3)     
