from fractions import *

numerator = 1
denominator = 1

for a in range(10,99):
    for b in range(a + 1,99):
        # Should probably check for cancellation of digits in
        # the opposite diagonal. But these found all 4, so moving on
        if a % 10 != int(float(b) / 10):
            continue;
        
        a2 = int(float(a) / 10)
        b2 = int(b % 10)

        if b2 != 0 and float(a2) / b2 == float(a) / b:
            numerator *= a
            denominator *= b
            print str(a) + '/' + str(b)

print 'Answer: ' + str(Fraction(numerator, denominator))
