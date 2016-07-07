import time
start=time.time()

f1=1
f2=1
fibo=0
index=2
while len(str(fibo))<1000:
	fibo=f1+f2
	index+=1
	f2=f1
	f1=fibo
print(index)

end=time.time()
print(str(round(end-start,4))+" seconds")
