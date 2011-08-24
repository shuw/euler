def answer(maxLength):
  current = 1
  increment = 0
  sum = 1 # count center
  while True:
    increment += 2

    if increment + 1 > maxLength:
      return sum
    
    current += increment # right lower
    sum += current
    current += increment # left lower
    sum += current
    current += increment # left upper
    sum += current
    current += increment # right upper
    sum += current
  

print (answer(1001))
