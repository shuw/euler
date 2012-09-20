from numbers import *

pList = list(pentagonal(10000000))
pSet = set(pList)

def answer():
    for i in range(len(pList)):
        p1 = pList[i]

        for j in range(i + 1, len(pList)):
            p2 = pList[j]
            if (p1 + p2) in pSet and (p2 - p1) in pSet:                
                return p2 - p1

print 'Answer: ' + str(answer())
