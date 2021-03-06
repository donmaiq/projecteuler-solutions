import time
start=time.time()

#get primes below n using sieves algorithm
def primes_below(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]


print(sum(primes_below(2000000)))

end=time.time()
print(str(round(end-start,3))+" seconds")
