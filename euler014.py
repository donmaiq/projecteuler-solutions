import time
start=time.time()

import time
start=time.time()

def chain_counter(number):
    chaincount=1
    match=False
    memory=[]
    while number!=1:
        memory.append(number)
        if known.get(number,False):
            chaincount+=known[number]
            break
        if number%2!=0:
            number=int(number*3+1)
        else:
            number=int(number/2)
        chaincount+=1
    memory.append(number)
    index=1
    for i in memory:
        if not known.get(i,False):
            known[i]=chaincount-index
        index+=1
    return chaincount

known={}
biggest_value=0
biggest_chain=0

chains=[]
for number in range(1,1000000):
    x=chain_counter(number)
    if x>biggest_chain:
        biggest_chain=x
        biggest_value=number
        
print(biggest_value)

end=time.time()
print(str(round(end-start,3))+" seconds")

