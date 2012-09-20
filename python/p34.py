from math import *
import copy

def sumOfAllNumbersEqualToFactorialOfDigits(digits, limit, sum):
    digitsInSum  = sorteddigits(sum)
    
    if sum > 2 and digits == digitsInSum:
        print(sum)
        return sum
    
    if len(digits) > len(digitsInSum):
        return 0

    answerSum = 0
    for i in reversed(range(limit + 1)):
        x = factorial(i) + sum
        d2 = copy.copy(digits)
        d2.append(i)
        answerSum += sumOfAllNumbersEqualToFactorialOfDigits(d2, i, x)
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

print('answer: ' + str(sumOfAllNumbersEqualToFactorialOfDigits([], 9, 0)))
