is_evenly_divisible = []

def prime(num):
	for i in range(2,num):
		if num % i == 0:
			is_evenly_divisible.append("not prime")
			break
	if "not prime" in is_evenly_divisible:
		print num, "is not prime"
	else:
		print num, "is prime"				

prime(10)

