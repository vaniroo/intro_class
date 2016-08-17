# str = "item:apples,quantity:4,price:1.50\n"
# str.split(',')

# split_string = str.split(',')
# split_string[2].split(':')

# price = split_string[2].split(':')


# print float(price[1])



# string parsing exercise part 2 start here #
# exercise 2.1
# my_name = "Vanessa"
# print list(my_name)

# exercise 2.2
# five = "1,2,3,4,5" 
# five_count = five.split(',')
# intlist =[int(x) for x in five_count]
# print intlist

# # exercise 2.3
# number_fish = "One fish two fish red fish blue fish"
# remove_fish = number_fish.replace("fish","")
# split_new_list = remove_fish.split("  ")
# print split_new_list

# exercise 2.4
items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]

items_divide = items[0].split(",")
print items_divide
itemss = items[0].split(":")
print itemss
more_items = itemss[2].split(",")
print more_items
#look at lecture and get rid of slash n and then make function to multiply the 4 and the 1.50 to get the total of bill, probably a for loop necessary
