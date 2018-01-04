from bisect import insort
from functools import reduce

def sieve(n):
  candidates = list(range(2, (n + 1)))
  prime_index = 0
  
  while prime_index < len(candidates) - 1:
    base_prime = candidates[prime_index]
    for x in candidates[(prime_index + 1):]:
      if x % base_prime == 0:
        candidates.remove(x)
    prime_index += 1
  
  return candidates

def factorize(n):
  possibilities = sieve(n)
  factors = []
  
  for p in possibilities:
    if n % p == 0:
      factors.append(p)
  
  prod = reduce(lambda x, y: x * y, factors)
  
  if prod == n:
    return factors
  else:
    quot = n // prod
    
    if quot in possibilities:
      insort(factors, quot)
      return factors
    else:
      for q in factorize(quot):
        insort(factors, q)
      return factors