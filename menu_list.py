menu_list = ["food:hotdog,price:5.50","food:burger,price:9.50",
       "food:fries,price:4.00","food:shake, price:5.00"]

menu_dict = {}

def menu_things():

	for item in menu_list:
		mini_list = item.split(",")
		price_split = mini_list[1].split(":")
		food_list = mini_list[0].split(":")
		menu_dict[food_list[1]] = price_split[1]
	return menu_dict
		

def main():
	print menu_things()

if __name__ == '__main__':
	main()