def isPalindrome(phrase):    
    phrase_letters = [c for c in phrase.lower()]
    return (phrase_letters == phrase_letters[::-1])




for i in range(900,1000):
    for j in range(900,1000):
        x = i * j
        if isPalindrome(str(x)):
            print str(i) + " "  + str(j) + " " + str(x)
            break
