import time
start=time.time()

#sum of divisors of n
def d(n):
	total=1
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			total+=i
			total+= n/i
	return total

amicable={}
for a in range(1,10000):
	b = d(a)
	if a!=b and d(b)==a:
		if not amicable.get(a,False):
			amicable[a]=b
			amicable[b]=a
print(sum(amicable.values()))	 



end=time.time()
print(str(round(end-start,4))+" seconds")
