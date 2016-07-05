import math
import time
start=time.time()

x = 3
primes=[2]

counter=1
while x<2000000:
	isprime=True
	for prime in primes:
		if prime>math.sqrt(x)+1:
			break
		if x%prime==0:
			isprime=False
			break
	if isprime:
		primes.append(x)
	if counter%200000==0:
		print(str(counter/10000)+"%")
	x+=2
	counter+=1
print("sum of "+str(len(primes))+" primes= "+str(sum(primes)))
end=time.time()
print(str(round(end-start,3))+" seconds")
