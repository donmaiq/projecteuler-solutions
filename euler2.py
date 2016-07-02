#summer

def is_multiple(number,multiple):
    if number%multiple == 0:
        return True
    else:
        return False

total_sum = 0
for x in range(0,1000):
    if is_multiple(x,3) or is_multiple(x,5):
        total_sum += x
print(total_sum)
