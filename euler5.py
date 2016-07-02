import time
import math

start = time.time()


l = 19*17*13*11*7*5*3*2
multiple = 2

def test(i):
    for c in range(2,21):
        if(i%c!=0):
            return False
    return True

while not test(l*multiple):
	test(l*multiple)
	multiple+=2
print(l*multiple)

end = time.time()
print(round(end - start,4),"seconds")
