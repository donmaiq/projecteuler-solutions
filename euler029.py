import time
start=time.time()

def a_b_powers(a, b):
	result = set()
	for x in range (a, b+1):
		for y in range (a, b+1):
			result.add(x**y)
	return result

print(len(a_b_powers(2,100)))

end=time.time()
print(str(round(end-start,3))+" seconds")