from math import *

for i in range(1, 1000):
    for j in range(i,1000):
        z2 = i*i + j*j
        z = sqrt(z2)
        if z % 1 == 0:
            z = int(z)
            print str(i) + '^2 + ' + str(j) + '^2 = ' + str(z) + '^2'
            if i + j + z == 1000:
                print 'finished ' + str(i * j * z)
                raise SystemExit
