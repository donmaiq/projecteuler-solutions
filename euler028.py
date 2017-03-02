import time
start=time.time()

def x_by_spiral(x):
	s = 0 #sum
	skip = 2 #skip this many for next corner
	next_corner = 1 #next corner
	corner_count = 0 #count corners and reset on 4
	for i in range(1, x*x+1):
		if i == next_corner:
			s += i
			next_corner += skip 
			corner_count += 1
		#reset corners and increase skip size
		if corner_count == 4:
			skip += 2
			corner_count = 0
	return s
	
print(x_by_spiral(1001))

end=time.time()
print(str(round(end-start,3))+" seconds")