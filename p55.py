import digits

def isLychrel(n):
    palindromeFound = False
    for i in range(50):
        # print str(n) + " " + str(digits.reverse(n)) + " " + str(n + digits.reverse(n))
        n = n + digits.reverse(n)
        if n == digits.reverse(n):
            palindromeFound = True
            break

    return not palindromeFound
        
def answer():
    count = 0
    for n in range (1,10000):    
        if isLychrel(n):
            # print n
            count += 1

    return count


print 'Answer: ' + str(answer())
