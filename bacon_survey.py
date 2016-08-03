def main():
	answer_1 = int(raw_input("Do you want to feel like angles are frolicking on your taste buds? Yes(1) or No(2) or Not sure(3)"))

	
	if answer_1 == 1:
		print "Eat it!"

	elif answer_1 == 2:
		print "You've clearly never tasted bacon."
		print "Eat it."
	else:
		print "I'm afraid bacon will kill me."
		answer_2 = int(raw_input("Are you a coward? Yes(1) or No(2)"))
		if answer_2 == 1:
			print "I am not"
			print "Then, eat it!"
		else:
			print "Yes, I am a coward."
			print "Bacon will turn you into a true warrior."

if __name__ == '__main__':
	main()