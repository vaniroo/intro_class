#nMake a dictionary and have the key equal the letter, and the value be the list with the corresponding numbers
#Make the function that calls the text file, and the match each row with the corresponding number/key, by iterating through the key values in our dictionary

Grades_Number = {"A":range(90,101,1),"B": range(80,90,1),"C": range(70,80,1),"D":range(60,70,1), "F": range(1,60,1)}

def read_file(file_name):
	with open(file_name)as my_file:
			output_list = my_file.readlines()
	return output_list
	

def match_file_to_dictionary()
	pass

def main
	pass

if __name__ == '__main__':
	main()


