palindromesSum = 0 # base 10 and base2
for n in range(1, 1000000):
  ndigits = list(str(n))
  ndigitsbin = list(bin(n)[2::])  

  if ndigits == list(reversed(ndigits)) or \
      ndigitsbin == list(reversed(ndigitsbin)):
    palindromesSum += n

print(palindromesSum)
