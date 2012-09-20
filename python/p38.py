from digits import *

largestPandigital = 0
# only 4 digit numbers need apply
for n in range(1, 10000):
    d = []
    i = 1    
    while True:
        m = n * i
        i += 1

        containsZero = False
        for md in toList(m):
            if md == 0:
                containsZero = True
            d.append(md)
            
        if len(d) > 9 or containsZero:
            break;
        elif len(d) == 9 and len(set(d)) == 9:
            panDigitalNumber = fromList(d)
            if panDigitalNumber > largestPandigital:
                largestPandigital = panDigitalNumber
                print largestPandigital
