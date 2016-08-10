
def count_letters():
	lettercount_dict = {}
	myname = "vanessa" #raw_input("What is your name?").lower()
	for letter in myname:

		if letter in lettercount_dict:
			lettercount_dict[letter] += 1
		else:
			lettercount_dict[letter] = 1


	print lettercount_dict
	pass
	

# count_letters()


prices = { "banana": 4, 
		   "apple": 2, 
		   "orange": 1.5, 
		   "pear": 3 }

# print prices
# print prices.keys()
# print prices.values()

highest_price = 0
highest_item = None

for item, price in prices.items():
	if price > highest_price:
		highest_price = price
		highest_item = item

print highest_item, "is the highest price at %s" % highest_price


