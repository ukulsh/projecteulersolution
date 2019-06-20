from itertools import permutations
def primes(n):
  """ return a list of prime numbers from 1 to < n """
  if n < 1:  return []
  if n == 1: return [1]
  if n == 2: return [2]
  # do only odd numbers starting at 3
  s = list(range(3, n, 2))
  # n**0.5 is supposed to be slightly faster than math.sqrt(n)
  mroot = n ** 0.5
  half = len(s)
  i = 0
  m = 3
  while m <= mroot:
    if s[i]:
      j = (m * m - 3)//2
      s[j] = 0
      while j < half:
        s[j] = 0
        j += m
    i = i + 1
    m = 2 * i + 3
  # make exception for unity and 2
  return [2]+[x for x in s if x]
a = primes(9999)
a = a[170:]
b = []
for i in range(len(a)):
  for j in range(i+1,len(a)):
    for k in range(j+1,len(a)):
      if a[j]-a[i] == a[k]-a[j]:
        if set(str(a[i])) == set(str(a[j])) and set(str(a[i])) ==set(str(a[k])):
          b.append((a[i],a[j],a[k]))
      if a[j]-a[i] < a[k]-a[j]:
        break
print(b)      


