from digits import *

pSet = {} # cache results

def doesChainEndAtEightyNine(n):
    if n == 89: return True
    elif n == 1: return False
    if n in pSet: return pSet[n]
    
    sum = 0
    for i in iterateDigits(n): sum += i**2
    result = pSet[sum] = doesChainEndAtEightyNine(sum)
    return result

count = 0
for n in range(1, 10000001):
    if doesChainEndAtEightyNine(n): count += 1

print 'Answer: ' + str(count)
        
