import time
start=time.time()

def findcycle(num):
	z=9
	decimals=1
	while z%num:
		z=z*10+9
		decimals+=1
		if decimals>num:
			return 0
	return decimals

max_d=0
max_v=0
for i in range(999,1,-1):
	if max_d>i:
		break
	d=findcycle(i)
	if d>max_d:
		max_d=d
		max_v=i

print(max_v)	

end=time.time()
print(str(round(end-start,4))+" seconds")
