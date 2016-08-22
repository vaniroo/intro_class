
shopping_list_dict = {"Target": ["bb cream", "soap", "detergent"], 
					"Safeway": ["milk", "cake", "cookies"], 
					 "Jane": ["chocolate", "popcorn", "soda"]}

def main_menu():
 #display list
	print """
	Choose a menu item:
	0 - Main Menu: 
	1 - Show all lists.
	2 - Show a specific list. 
	3 - Add a new shopping list. 
	4 - Add an item to a shopping list. 
	5 - Remove an item from a shopping list. 
	6 - Remove a list by nickname. 
	7 - Exit when you are done. 
	""" 
def user_choice():
	choice = int(raw_input("Choose a number from main menu: "))
	return choice

def show_all_lists(): #1
 #show items, keys and values, in alphabetical order
 	print shopping_list_dict

def show_specific_list(store): #2
#show items, all values, on a selected list
	return shopping_list_dict[store]
	

def add_new_shopping_list(store): #3
# add new shopping list, key has to be unique
	if store in shopping_list_dict:
		print "%s is already included" 

	shopping_list_dict[store] = []
	return shopping_list_dict


def add_item(store, new_item): #4
#adding item to an existing shopping list, cannot be duplicate
#print out all items from list
#ask user  for item until one is done
	
	for one_list in shopping_list_dict.values():
		if new_item in one_list:
			print "%s is already in your list" % new_item
	
	shopping_list_dict[store].append(new_item)
	print "%s has been added to the %s list" % (new_item,store)
	return shopping_list_dict[store]
		

def remove_item(remove_from_list): #5
#remove item from existing shopping list, cannot be duplicate
#print out all items from list
# ask user for item until one is done
	
	for store, store_list in shopping_list_dict.items():
		if remove_from_list in store_list:
			shopping_list_dict[store].remove(remove_from_list)
			return "this is your updated shopping list", shopping_list_dict[store]


	return " %s item is not currently in your shopping list" % remove_from_list



def remove_list_nickname(store): #6
#remove list based on entered nickname or key
	if store not in shopping_list_dict:
		return "this store in not part of your list"
	else:

		del shopping_list_dict[store]
		print "%s has been deleted. these are you current shopping lists" % store
		return shopping_list_dict


def exit_done(): #7
#exit from shopping list
	print "Thanks for using shopping list app!"
	print "Bye-bye!"
	


def main():
	while True:
		main_menu()
		choice = user_choice()

		if choice == 1:
			show_all_lists()
		if choice == 2:
			print "These are the stores with lists"
			print shopping_list_dict.keys()
			store_name = raw_input("Please, pick a store ")
			print "here are the items for this store"
			print show_specific_list(store_name)
		if choice == 3:
			store = raw_input("what new store would you like to add?\n")
			print add_new_shopping_list(store)
		if choice == 4:
			item = raw_input("what item would you like to add?")
			store_name = raw_input("what store would you like to add it to?")
			print add_item(store_name,item)
		if choice == 5:
			remove_from_list = raw_input("what item do you want to remove")
			print remove_item(remove_from_list)
		if choice == 6:
			store = raw_input("what store do you want to remove?")
			print remove_list_nickname(store)
		if choice == 7:
			exit_done()
			break


	
if __name__ == '__main__':
	main()