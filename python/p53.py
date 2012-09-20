from math import *

upTo = 100

factorials = [0]*(upTo+1)
factorials[0] = 1

count = 0
for n in range(1, upTo + 1):
    factorials[n] = factorials[n-1] * n

    # start at maximum value
    nHalf = int(ceil(n / 2.0))
    for r in range(nHalf, n):
        nCr = (factorials[n] / factorials[r]) / factorials[n - r]
        if nCr > 1000000:
            # print 'n=' + str(n) + ' r=' + str(r) + ' nCr=' + str(nCr)
            if r == nHalf and n % 2 == 0:
                count += 1
            else:
                count += 2
        else:
            break
    # print str(n) + ' c1:' + str(count) + ' c2:' + str(count2)

print 'Answer :' + str(count)
