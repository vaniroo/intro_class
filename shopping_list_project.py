
	
def add_to_list(shopping_list):
	item = raw_input("What would you like to add?")
	item.lower()
	if item in shopping_list:

		print "This item is already in your list."
	else:
	 	shopping_list.append(item)
		shopping_list.sort()

	return shopping_list

def order_list(shopping_list):
	shopping_list.sort()

	print shopping_list
	return shopping_list

def remove_item(shopping_list):
	print shopping_list
	item2 = raw_input("what do you want to remove?").lower()
	
	if item2 in shopping_list:
		shopping_list.remove(item2)
	else:
		print "it is not there"
	
	shopping_list.sort()
	print shopping_list
	return shopping_list

def main():
	import time
	shopping_list = ["tomatoes","chicken","rice"]
	
	print "let's make a shopping list"
	add_to_list(shopping_list)
	print shopping_list
	time.sleep(2)
	order_list(shopping_list)
	print shopping_list
	time.sleep(2)

	remove_item(shopping_list)
	print shopping_list
	time.sleep(2)

	shopping_list.extend(["mandarin","apple","orange","meat"])
	print shopping_list
	time.sleep(2)

	shopping_list.remove("apple")
	print shopping_list
	time.sleep(2)

	shopping_list.remove("meat")
	print shopping_list
	

if __name__ == '__main__':
	main( )