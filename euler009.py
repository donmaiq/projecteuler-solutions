import time
start=time.time()

def is_triplet(array):
	array.sort()
	if array[0]<array[1]<array[2] and array[0]**2+array[1]**2==array[2]**2:
		return True
	return False

c=4
correct=[]
found=False
#find a pythagoran that is divisible by 1000
while not found:
	power=c**2
	for b in range(c,1,-1):
		for a in range(c-1,1,-1):
			if is_triplet([a,b,c]) and (1000/(a+b+c))%1==0:
				tmp=1000/(a+b+c)
				if (tmp*a)+(tmp*b)+(tmp*c)==1000:
					found=True
					correct=[tmp*a,tmp*b,tmp*c]
					break
	c+=1
print(correct)
print(correct[0]*correct[1]*correct[2])
end=time.time()
print(str(end-start)+" seconds")
