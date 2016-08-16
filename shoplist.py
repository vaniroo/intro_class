
shopping_list_dict = {"Target": ["socks", "soap", "detergent", "sponges"], 
					"Safeway": ["butter", "cake", "cookies", "bread"], 
					# "PeterGrocery": ["apples", "oranges", "bananas", "milk"], 
					"JaneGrocery": ["oreos", "brownies", "soda"]}
					


# def user_choice():
# 	choice = int(raw_input("Choose a number from main menu:"))
# 	return int(choice)

# choice = int(raw_input("Choose a number from main menu:"))
# 	return int(choice)

def show_all_lists():
 #show items, keys and values, in alphabetical order
 	print shopping_list_dict

def show_specific_list(shopping_list_dict):
#show items, all values,on a selected list
	print "These are the lists:",shopping_list_dict.keys()
	print shopping_list_dict[raw_input("which list would you like to see?")]
	

def add_new_shopping_list(key):
	key = key
	shopping_list = []
# add new shopping list, key has to be unique
	# print shopping_list_dict[raw_input("which list would you like to add?")]
	if key not in shopping_list_dict:
		shopping_list_dict[key] = shopping_list
	else:
		print "A list with that name already exists"

def add_item(key,item):
#adding item to an existing shopping list, cannot be duplicate
#print out all items from list
#ask user  for item until one is done
	item = item.lower()
	key = key.lower()
	if key in shopping_list_dict:
		shopping_list = shopping_list_dict[key]

		if item not in shopping_list:
			shopping_list.append(item)
			print "here is your updated list", sorted_shopping_list(key)
		else:
			print "this item %s already exists" % (item)
	else:
		print "There is no list with that name."


	# new_item = raw_input("what item do you want to add to your list?").lower()
	# for one_list in shopping_list_dict.values():
	# 	#for new_item in one_list:
	# 	new_list = raw_input("where do you want to add it?")
	# 	one_list.append(new_item)
	# # print one_list
#print "%s is already in your list" % new_item
	#new_item is the value
	#need to specify which key new_item goes into

	
		

def remove_item(shopping_list_dict):
#remove item from existing shopping list, cannot be duplicate
#print out all items from list
# ask user for item until one is done
	remove_from_list = raw_input("what do you want to remove:")
	for one_list in shopping_list_dict.values():
		if remove_from_list in one_list:
			one_list.remove(remove_from_list)
			print one_list

def remove_list_nickname(shopping_list_dict):
#remove list based on entered nickname or key
	del shopping_list_dict["Target"]
	print shopping_list_dict
	

def exit_done(shopping_list_dict):
#exit from shopping list
	print "Thanks for using shopping list app!"
	print "Bye-bye!"
	

def main():
	# all functions work independently with hard coded data
	# TODO: change hard coded data into raw_input data saved into variable
	# TODO: pass variables into functions as arguments when being called
	# TODO: give functions paramater so it can use variables from raw_input
	# TODO: make a while loop that works and is not infinite
	# user_choice()
	choice = None
  	while choice != 7:
  		choice = main_menu()
  		if choice == 1:
  			print shopping_list_dict
  		elif choice == 2:
  			show_specific_list(shopping_list_dict)
  		elif choice == 3:
  			list_name = raw_input("which list would you like to see?")
  			add_new_shopping_list(list_name)
  			item = raw_input("please enter an item")
  			choice = 0
  		elif choice == 4:
  			add_item(shopping_list_dict)
  		elif choice == 5:
  			remove_item(shopping_list_dict)
  		elif choice == 6:
  			remove_list_nickname(shopping_list_dict)
  		else: 
  			print "bye"
       	


def main_menu():
	while True:
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
		choice = raw_input("-->  ")
		# if choice not in str(range(8)):
		# 	print "'" + str(choice) + "' was not a menu item."
		# else:
		return int(choice)   			
		
	
if __name__ == '__main__':
	main()
