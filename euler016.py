import time
start=time.time()

print(sum(int(i) for i in str(2**1000)))

end=time.time()
print(str(round(end-start,3))+" seconds")
