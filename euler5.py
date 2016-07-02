import time
start = time.time()

def is_divisible(arg):
    for x in range(2,21):
        if arg%x != 0:
            return False
    return True

searching = True
inc=0
while True:
    inc += 380 #increment with product of 19 and 20
    if is_divisible(inc):
        break
print(inc)
    
end = time.time()
print(round(end - start,4),"seconds")

