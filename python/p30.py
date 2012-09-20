from math import *
import copy

def sumOfAllNumbersEqualToPowerOfDigits(p, digits, limit, sum):
    digitsInSum  = sorteddigits(sum)
    
    if sum > 1 and digits == digitsInSum:
        print(sum)
        return sum
    
    if len(digits) > len(digitsInSum):
        return 0

    answerSum = 0
    for i in reversed(range(limit + 1)):
        x = int(pow(i, p) + sum)
        d2 = copy.copy(digits)
        d2.append(i)
        answerSum += sumOfAllNumbersEqualToPowerOfDigits(p, d2, i, x)
        # print(str(d2) + " -> " + str(int(x)))

    return answerSum


def sorteddigits(n):
    d = []
    while n > 0:
        d.append(n % 10)
        n = int(n / 10)

    d.sort()
    d.reverse()
    return d

# print(sorteddigits(23436725))


print('answer: ' + str(sumOfAllNumbersEqualToPowerOfDigits(5, [], 9, 0)))
