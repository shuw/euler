from data.p42_words import *


# find 1000 triangle numbers, should be more than enough
triangleNumbers = set(int((n*n + n) / 2) for n in range (1, 1000))


def value(word):
    r = 0
    for letter in word:
        r += ord(letter) - 64
    return r

def answer():
    count = 0
    for word in words:
        if value(word) in triangleNumbers:
            count += 1
            print word
    return count

print 'Answer: ' + str(answer())


    
        
