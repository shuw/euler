def getFactors(n):
    i = 1;
    factors = 0
    while True:
        if i > n:
            return factors
        if (n / float(i)) % 1 == 0:
            factors += 1            
        i+=1

i = 1000000
while True:
    t = (i^i + i) / 2
    
    factors = getFactors(t)
    print factors
    if factors > 500:
        print 'answer' + str(t)
        break
    
    i += 1
    
