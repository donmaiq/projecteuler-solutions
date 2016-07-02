import time
import math
start = time.time()

omitted=0

def consecutive(value):
    counter=0
    previous=""
    for i in range(0,len(value)):
        if value[i]==previous:
            counter+=1
        else:
            counter=0
        if counter==2:
            return True
        previous=value[i]
    return False


total = 1
cycles = 1000000000
counter=0
counter2=0
for x in range(2,cycles):
    if consecutive(str(x)):
        omitted += 1
        continue
    else:
        total += 1/x
    if counter==cycles/100:
        counter2+=1
        print(str(counter2)+"/"+str(int(cycles/(cycles/100))))
        counter=0
    counter += 1

print(total)

end = time.time()
print(round(end - start,4),"seconds")


