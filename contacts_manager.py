import contact

def main():
	contact_list = []
	print "Add a new contact"
	add_first_name = raw_input("What is your first name")
	add_last_name = raw_input("What is your last name")
	add_mobile_number = raw_input("What is your mobile number")
	add_email = raw_input("What is your email address")

	new_contact = contact.Contact(first_name = add_first_name, last_name = add_last_name, mobile_number = add_mobile_number, email = add_email)

	contact_list.append(new_contact)


	for person in contact_list:
		print person.first_name
		print person.last_name
		print person.mobile_number
		print person.email


if __name__ == '__main__':
	main()