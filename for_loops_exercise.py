# for item in range (1,21):
# 	print item,

# for item in range (1,21):
# 	if item == 13:
# 		print "Hello"
# 	else:
# 		print item

# fruits = ['apples','oranges','bananas']
# # for item in fruits:
# # 	print item
# for item in range(len(fruits)):
# 	#print fruits[0]
# 	print fruits[item]
def add_to_list(shopping_list):
	item = raw_input("What would you like to add?")
	item = item.lower()
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

def menu(shopping_list):
	print shopping_list
	while True:
		option = int (raw_input("Write 1 for main menu, 2 for show current list or 3 for add item"))
		if option == 1:
			print "main menu"
		elif option == 2:
			print " show current list"
		elif option ==3:
			print "add am item to shopping list"
		else:
			print "exit"
			break



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
	
	menu(shopping_list)
	index = 0
	while ((index < len(shopping_list))):
		print shopping_list[index]
		index += 1

if __name__ == '__main__':
	main( )




	