import time
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

t=time.time()
primeb=primes(1000)
prime=primes(10000)
m=0
for b in primeb:
    for a in range(-b,1000):
        n=0
        while n**2+a*n+b in prime:
            n+=1
        n-=1
        if n>m:
            print ('n^2+'+str(a)+'n+'+str(b), n)
            m=n
print (m, time.time()-t)