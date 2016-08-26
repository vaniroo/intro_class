"""
Create a contact list and do the following:
1. Add a couple contacts.
2. Change the mobile number for one of the contacts to 888-888-8888.
3. Change the last name of one of your contacts to "Williams"

"""

contacts = {"Pete Gardener": "(916)589-4552","Tess Grady": "(530)566-7887", "Diana Banana": "(415)555-5555"}


def add_contact(contacts):
	for key in contacts:


		name = raw_input("what name would you like to add?")
		phone_number = raw_input("what phone number do you want to add?")

	contacts[name] = phone_number
	print contacts.items()

def change_number():
	pass

def change_lastname():
	pass





def main():



	if __name__ == '__main__':
		main()