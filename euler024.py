import time
import math
start=time.time()

array=[0,1,2,3,4,5,6,7,8,9]
result=[]
limit=1000000
for i in range(len(array)-1,-1,-1):
	#append to result in order of largest numbers left
	if limit==0:
		result.append(array[-1])
		array.remove(array[-1])
		continue
	#append to result in order of smallest numbers left
	elif limit==1:
		result.append(array[0])
		array.remove(array[0])
		continue
	
	#limit divided by arrangements of numbers in array-1
	#if below or 1 then take first number in array
	#else take steps index from array and calculate remaining limit
	if float(limit)/math.factorial(i)>1:
		steps = int(math.ceil(float(limit)/math.factorial(i)))-1
		limit = limit%(math.factorial(i))
	else:
		steps=0	
	result.append(array[steps])
	array.remove(array[steps])

def tostring(arg):
	string=""
	for i in arg:
		string+=str(i)
	return string

print(tostring(result))
end=time.time()
print(str(round(end-start,4))+" seconds")


#01234 01243 01324 01342 01423 01432
# 0 1 2 3 4  limit 5				# 0 1 2 3 4  limit 6
# _ _ _ _ _  4!=24 -> 5/24=0			# _ _ _ _ _  4!=24 -> 6/24=0

# _ 1 2 3 4  limit 5				# _ 1 2 3 4  limit 6
# 0 _ _ _ _  3!=6 -> 5/6=0			# 0 _ _ _ _  3!=6 -> 6/6= 0 (<1)
		
# _ _ 2 3 4  limit 5				# _ _ 2 3 4  limit 6
# 0 1 _ _ _  2!=2 -> 5/2=2.5 ->3		# 0 1 _ _ _  2!=2 -> 6/2=3

# _ _ 2 3 _  limit 1=fill from left 		# _ _ 2 3 _  limit 0= fill from right
# 0 1 4 _ _  					# 0 1 4 _ _ 
