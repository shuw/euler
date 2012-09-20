from digits import *

n = [1,2,3,4,5,6,7,8,9]
nSet = set(n)

products = set()
s = 0
for lhs in choose(n, 5):
    for x in range(3,5):
        for m1 in permutate(list(lhs), x):
            m1n = fromList(m1)
            m2Digits = list(set(lhs) - set(m1))
            for m2 in permutate(m2Digits, len(m2Digits)):
                m2n = fromList(m2)
                product = m1n * m2n

                together = toList(product) + list(m1) + list(m2)    
                if len(together) == len(set(together) - set([0])) == 9:
                    if product not in products:
                        s += product
                        products.add(product)
                    
                    print str(m1n) + " " + str(m2n) + " " + str(product)
            
print 'Answer (excluding duplicate products): ' + str(s)
