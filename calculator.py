def add(num1,num2):
	return num1+num2

def subtract(num1,num2):
	return num1-num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1,num2):
	return num1/num2

def modulo(num1,num2):
	return num1 % num2

def power(base, exponent):
	return base**exponent

def square(num):
	return num**2



print add(4,5)
print subtract(4,5)
print multiply(4,5)
print divide(5,4)
print modulo(5,7)
print power(2,3)
print square(2)
print power(2,3)**2

print add(4,5) + subtract(9,6)
print divide(12,2) - 60
print add(1,2) + 3
print add(1,2)**2
print modulo(3,4)/ multiply(9,9)
print add(3,8)* 7
print 7*add(3,8)
print add(1,2) - 3 * add(4,5)
print 3**add(2,3)