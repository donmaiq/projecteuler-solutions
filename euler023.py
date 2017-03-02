#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import time
start=time.time()

def is_abundant(num):
	if num < 12: return False
	total = 1
	root = int(num**0.5)
	for i in range(2, root+1):
		if num % i == 0:
			total += i + num/i
	if root*root==num: total -= root
	if num < total:
		return True
	return False

abundants = set()
sum_of_not = 0

for i in range(1, 28124):
	has_sum = False
	for abundant in abundants:
		if i-abundant in abundants:
			has_sum = True
			break
	if not has_sum: sum_of_not += i
	if is_abundant(i):
		abundants.add(i)

print("Sum of numbers that cannot be written with as sum of two abunants:")
print(sum_of_not)

end=time.time()
print(str(round(end-start,3))+" seconds")