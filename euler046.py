import time
start=time.time()
# n = a + 2 * b**2

def components(n):
	for a in primes:
		if a+2>n:
			break
		for b in range(1,int(n**0.5)):
				if n==a+(2*(b**2)):
					return True
	return False

def initarrays():
	c=3
	primearray=[2]
	compositearray=[]
	while len(primearray)<1000:
		prime=True
		for x in range(2,int(c**0.5)+1):
			if c%x==0:
				prime=False
				break
		if prime==True:
			primearray.append(c)
		else:
			compositearray.append(c)
		c+=2
	return primearray,compositearray


primes,composites=initarrays()

def main():
	for i in composites:
		if not components(i):
			return i
	return -1
print(main())


end=time.time()
print(str(round(end-start,4))+" seconds")
