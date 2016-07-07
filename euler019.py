import time
start=time.time()

sundays=0
day=1
year=1901
months=[31,28,31,30,31,30,31,31,30,31,30,31]
while year!=2001:
	for month in months:
		if month==28:
			if year%100==0:
				if year%400==0:
					month+=1
			elif year%4==0:
				month+=1
		for days in range(1,month):
			if day==7 and days==1:
				sundays+=1
			if day==7:
				day=1
			else:
				day+=1
	year+=1

print(sundays)

end=time.time()
print(str(round(end-start,4))+" seconds")
