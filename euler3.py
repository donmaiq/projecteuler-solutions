import time
import math
start = time.time()

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

print(int(max(prime_factors(600851475143))))

end = time.time()
print(round(end - start,4),"seconds")


