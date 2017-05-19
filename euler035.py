import time
start=time.time()

from math import log, ceil

def rotations(n):
  rotations = set()
  length = int(ceil(log(n, 10)))
  if length == 1:
    rotations.add(n)
    return rotations
  for i in range(length - 1):
    if n % 2 == 0 or n % 5 == 0:
      return False
    rotation = (n%10)*10**(length-1) + n // 10
    rotations.add(rotation)
    n = rotation
  return rotations

def primes_below(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primes = primes_below(1000000)
circular_primes = 0
for i in primes:
  r = rotations(i)
  if not r:
    continue
  is_circular = True
  for a in r:
    if not a in primes:
      is_circular = False
      break
  if is_circular:
    print(i)
    circular_primes += 1

print("result:",circular_primes)

end=time.time()
print(str(round(end-start,3))+" seconds")