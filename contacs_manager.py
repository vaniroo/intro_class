import contact

def add_new_contact(first_name, last_name, mobile_phone=’’, email=’’):
    # handle cases and whitespace for name parameters
    first_name = first_name.upper().strip()
    last_name = last_name.upper().strip()
    # handle if contact_list is empty
    if contact not in contact_list:
        new_contact = contact.Contact(first_name = add_first_name, last_name = add_last_name, mobile_phone = add_mobile_number, email = add_mobile_number)
        contact_list.append(new_contact)
    else:
        print "Contact is already on the list."
    # iterate contact_list, check if contact already exists, print error
    # instantiate instance of Contact
    # add to contacts_list

def edit_contact()

    first_name = first_name.upper().strip()
    last_name = last_name.upper().strip()

    for contact in contact_list:
        #check if contact.firstname == first_name && last 








    # if contact in contact_list:
    #     edit_contact = contact.Contact(first_name = edit_first_name, last_name = edit_last_name, mobile_phone = edit_mobile_number, email = edit_mobile_number)
    #     contact_list.append(edit_contact)
   

def delete_contact():
    #delete contact from list
       if contact in contact_list:
        edit_contact = contact.Contact(first_name = delete_first_name, last_name = delete_last_name, mobile_phone = delete_mobile_number, email = delete_mobile_number)
        contact_list.remove(edit_contact)

def current_contacts():
   pass




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