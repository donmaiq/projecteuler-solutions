import time
start=time.time()

def sum_of_powered_num(target_power):
  s = 0
  for i in range(2, 10**(target_power+1)):
    char_sum = 0
    num = i
    while num:
      num, char = num // 10, num % 10
      char_sum += char**target_power
    if char_sum == i:
      s += i
  return s

print(sum_of_powered_num(5))

end=time.time()
print(str(round(end-start,3))+" seconds")