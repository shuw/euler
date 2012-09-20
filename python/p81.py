import numpy
from math import *

def move(a, i, j, answers):
    if answers[i][j] != 0: return answers[i][j]
    
    atBottom, atRight = (i+1 == len(a), j+1 == len(a[0]))

    v, nextV = (a[i][j], 0)
    if atBottom and atRight: return v
    if atBottom: nextV = move(a, i, j+1, answers)
    elif atRight: nextV = move(a, i+1, j, answers)
    else:    
        down = move(a, i+1, j, answers)
        right = move(a, i, j+1, answers)
        nextV = down if down < right else right

    answers[i][j] = nextV + v
    return answers[i][j]    
    

def answer(a): return move(a, 0, 0, numpy.zeros((len(a),len(a[0])), dtype=int))

fileName = 'data/p81_matrix.txt'
numbers = tuple((tuple(int(n) for n in v.split(',')) for v in open(fileName)))

print answer(numbers)
