def reading_foods(fave_food):
	with open(fave_food) as my_file:
		output = my_file.readlines()
		return output

def compare_favs(vanessa_favs, noelis_favs):
	if vanessa_favs[0] == noelis_favs[0]:
		print "Our favorite foods are the same!"
	else:
		print "Our favorite foods are different"

def main():
	vanessa_favs = reading_foods("vanessa_fav_foods.txt")
	noelis_favs = reading_foods("noelis_fav_foods.txt")

	# print vanessa_favs
	# print noelis_favs

	compare_favs(vanessa_favs, noelis_favs)

if __name__ == '__main__':
	main()