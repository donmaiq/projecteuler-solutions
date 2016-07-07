import time
start=time.time()

def factorial(num):
	total=num
	for i in range(num-1,1,-1):
		total *= i
	return total

def sumofindex(num):
	total=0
	for i in range(0,len(str(num))):
		total+=	int(str(num)[i])
	return total

print(sumofindex(factorial(100)))

end=time.time()
print(str(round(end-start,4))+" seconds")
