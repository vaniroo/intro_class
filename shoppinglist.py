shopping_list_list = {"Target":["socks", "soap", "detergent", "sponges"], "Safeway":["butter", "cake", "cookies", "bread"], "PeterGrocery": ["apples", "oranges", "bananas", "milk"], "JaneGrocery": ["oreos", "brownies", "soda"]}

def main_menu():
 #display list
 	pass

def show_all_lists():
 #show items, keys and values, in alphabetical order
 	pass

def show_specific_list():
#show items, all values, on a selected list
	pass

def add_new_shopping_list():
# add new shopping list, key has to be unique
	pass

def add_item(key, value):
#adding item to an existing shopping list, cannot be duplicate
#print out all items from list
#ask user  for item until one is done
	pass

def remove_item(value):
#remove item from existing shopping list, cannot be duplicate
#print out all items from list
# ask user for item until one is done
	pass

def remove_list_nickname():
#remove list based on entered nickname or key
	pass

def exit_done():
#exit from shopping list
	pass


def main():
	menuchoice = int(raw_input("Choose a menu item: 0 - Main Menu: 1 - Show all lists. 2 - Show a specific list. 3 - Add a new shopping list. 4 - Add an item to a shopping list. 5 - Remove an item from a shopping list. 6 - Remove a list by nickname. 7 - Exit when you are done. "))
	while menuchoice != 7:

		if menuchoice == 2:
			print shopping_list_list.keys() 
			break
		else:

			break



if __name__ == '__main__':
	main()