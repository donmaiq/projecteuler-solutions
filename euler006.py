import time
start = time.time()

squaresum = 0
for x in range(1,101):
    squaresum += x
squaresum *= squaresum

summ = 0
for x in range(1,101):
    summ += x*x
    
difference = squaresum - summ
print(difference)

end = time.time()
print(end - start,"seconds")
