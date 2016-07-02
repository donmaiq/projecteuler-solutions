import time
import math

start = time.time()

i=0
C=3
nth_prime = 10001

while i<nth_prime:
    prime=True
    for x in range(2,int(math.sqrt(C))+1):
        if C%x==0:
            prime=False
            break
    if prime==True:
        i+=1
        number=C
    C+=2
    
print(str(nth_prime)+"th primenumber is: "+str(number))

end = time.time()
print(round(end - start,4),"seconds")
