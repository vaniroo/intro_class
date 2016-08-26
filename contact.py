class Contact(object):
	def __init__(self, first_name, last_name, mobile_number = "", work_number = "", email = ""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile_number = mobile_number
		self.work_number = work_number
		self.email = email


	def send_text(self, message):
		if self.mobile_number != "":
			print "To: %s - %s" % (self.mobile_number, message)
		else:
			print "No mobile number is provided"


def main():

	contact_jasmin = Contact(first_name = "Jasmin", last_name = "Herrera", email = "itsjasmin@gmail.com", mobile_number = "9253004462")
	contact_vanessa = Contact(first_name = "Vanessa", last_name = "Roman")
	contact_peter = Contact(first_name = "Peter", last_name = "Akiyama")

	contact_list = []
	contact_list.append(contact_jasmin)
	contact_list.append(contact_vanessa)
	contact_list.append(contact_peter)	

	for contact in contact_list:
		print contact.first_name
		contact.send_text("Hi! How are you?")


if __name__ == '__main__':
	main()