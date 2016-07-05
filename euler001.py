import time
start = time.time()

result=0
for i in range(1,1000):
    if not i%3 or not i%5:
        result += i
print(result)

end = time.time()
print(round(end - start,4),"seconds")

