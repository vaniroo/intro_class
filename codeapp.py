
def read_file_by_iteration(file_name):
	# output_list = []
	with open(file_name)as my_file:
		output = my_file.read()
		# for line in my_file:
		# 	clean_line = line.strip()
		# 	output_list.append(clean_line)
	return output


def split_string(intake_string):
	word_list = intake_string.split()
	return word_list

def clean_words(word_list):
	cleaned_words = []
	
	for word in word_list:
		word = word.strip('.')
		word = word.strip(',')
		word = word.strip('\xef\xbb\xbf')
		word = word.lower()
		cleaned_words.append(word)
	return cleaned_words




def count_duplicate_words(cleaned_words_list):
	word_dictionary_count = {}

	for word in cleaned_words_list:
		if word not in word_dictionary_count:
			word_dictionary_count[word] = 1
		if word in word_dictionary_count:
			word_dictionary_count[word] += 1

	return word_dictionary_count


def write_to_file(word_dictionary):

	with open("word_count.txt", mode = "w") as my_file:
		for word, count in sorted(word_dictionary.items()):
			word_string = word + " " + str(count) + '\n'
			my_file.write(word_string)


def main():
	file_name = "LoremIpsum.txt"
	intake_string = read_file_by_iteration(file_name)
	word_list = split_string(intake_string)
	cleaned_words = clean_words(word_list)
	word_dictionary = count_duplicate_words(cleaned_words)
	print write_to_file(word_dictionary)
if __name__ == '__main__':
	main()

