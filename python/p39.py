import primes
import math
import time

def answer():
    counts = [0]*1001

    for a in range(1, 1000):
        for b in range(1, 1000):
            c = math.sqrt(a*a + b*b)

            if a + b + c > 1000:
                break
            
            if c % 1 == 0:
                counts[int(a + b + c)] += 1

    print counts.index(max(counts))

answer()
