import math

n = 0
pos = 0
d = 1
p = 1
while True:
    n += 1
    nStr = str(n)
    numLength = len(nStr)
    pos += numLength

    if pos >= d:
        digit = int(nStr[numLength - pos + d - 1])
        print digit
        p *= digit
        d *= 10

        if d > 1000000:
            break

print 'Answer: ' + str(p)
