from math import *

def lastTenDigitsOfSeries(upTo):
    sum = 0
    for n in range(1,upTo + 1):    
        x = 1
        for i in range(n):
            x = (x * n) % 10000000000
        sum = (sum + x) % 10000000000

    return sum

print lastTenDigitsOfSeries(1000)
