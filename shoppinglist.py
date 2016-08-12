shopping_list_dict = {"Target": ["socks", "soap", "detergent", "sponges"], 
					"Safeway": ["butter", "cake", "cookies", "bread"], 
					"PeterGrocery": ["apples", "oranges", "bananas", "milk"], 
					"JaneGrocery": ["oreos", "brownies", "soda"]
					}

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
	choice = int(raw_input("Choose a number from main menu"))
	return choice

def show_all_lists():
 #show items, keys and values, in alphabetical order
 	print shopping_list_dict

def show_specific_list():
#show items, all values, on a selected list
	print shopping_list_dict["Target"]
	

def add_new_shopping_list():
# add new shopping list, key has to be unique
	shopping_list_dict["Walgreens"] = []
	return shopping_list_dict

def add_item():
#adding item to an existing shopping list, cannot be duplicate
#print out all items from list
#ask user  for item until one is done
	new_item = "soap" #raw_input("what item do you want to add to your list?")
	
	for one_list in shopping_list_dict.values():
		if new_item in one_list:
			print "%s is already in your list" % new_item
			print one_list
		

def remove_item():
#remove item from existing shopping list, cannot be duplicate
#print out all items from list
# ask user for item until one is done
	remove_from_list = "oreos" #raw_input("what do you want to remove")
	for one_list in shopping_list_dict.values():
		if remove_from_list in one_list:
			one_list.remove(remove_from_list)
			print one_list

def remove_list_nickname():
#remove list based on entered nickname or key
	del shopping_list_dict["Target"]
	print shopping_list_dict
	

def exit_done():
#exit from shopping list
	print "Thanks for using shopping list app!"
	print "Bye-bye!"
	

def main():
	# all functions work independently with hard coded data
	# TODO: change hard coded data into raw_input data saved into variable
	# TODO: pass variables into functions as arguments when being called
	# TODO: give functions paramater so it can use variables from raw_input
	# TODO: make a while loop that works and is not infinite
	
	main_menu()
	choice = user_choice()

		
	show_all_lists()

		
	show_specific_list()
	print add_new_shopping_list()
	print remove_item()
	print remove_list_nickname()
	add_item()
	
	exit_done()
	
if __name__ == '__main__':
	main()