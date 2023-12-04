errorMarg = 0.1
a = 0.5
b = 1

funcA = a**3 - 9*a + 5
funcB = b**3 - 9*b + 5
c = ((a * funcA) - (b*funcB)) / (funcA - funcB)
funcC = c**3 - 9*c + 5
while (b - a) >= errorMarg:
  funcA = a**3 - 9*a + 5
  funcB = b**3 - 9*b + 5
  funcC = c**3 - 9*c + 5
  if funcA * funcC > 0:
    a = c
  if funcB * funcC > 0:
    b = c
  c = ((a * funcA) - (b*funcB)) / (funcA - funcB)



result = ((a * funcA) - (b*funcB)) / (funcA - funcB)
print("{:.3f}".format(result))