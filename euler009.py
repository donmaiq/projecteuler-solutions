import time
start=time.time()

def is_triplet(array):
	array.sort()
	if array[0]<array[1]<array[2] and array[0]**2+array[1]**2==array[2]**2:
		return True
	return False

def triplet_equals(array,num):
	if sum(array)==num:
		return True
	return False

c=4
correct=[]
found=False
while not found:
	power=c**2
	for b in range(c,1,-1):
		for a in range(c-1,1,-1):
			if is_triplet([a,b,c]) and triplet_equals([a,b,c],1000):
				correct=[a,b,c]
				found=True
				break
	c+=1
	print(c)
print(correct)
end=time.time()
print(str(end-start)+" seconds")
