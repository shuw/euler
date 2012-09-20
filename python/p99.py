from math import *

numbersFile = open('data/p99_base_exp.txt')
numbers = (tuple(int(n) for n in v.split(',')) for v in numbersFile)

count, maxL = (0, 0)
for n in numbers:
    count += 1
    l = log(n[0], 10) * n[1]
    if l > maxL:
        maxL = l
        print '10^%f - lineNumber #%d' % (l, count)
