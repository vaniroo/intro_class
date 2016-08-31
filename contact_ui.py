import contact_manager

def main_menu():

    print """
    Choose a menu item:
    0 - Main Menu
    1 - Show all contacts
    2 - Add a new contact
    3 - Edit a contact
    4 - Delete a contact
    5 - Exit the program
    """


def main():
    while True:
        main_menu()
        choice = user_choice()

        if choice == 1:
            #show all contacts
            current_contacts()

        if choice == 2:
            # add a new contact list
            add_new_contact = raw_input("what new contact would you like to add?\n")
            print add_new_contact(contact)

        if choice == 3:
            #edit a contact
            edit_contact_first = raw_input("which contact would you like to edit?\n")
            edit_contact_last= raw_input("which contact would you like to edit?\n")
            contact_manager.edit_contact(edit_contact_first, edit_contact_last)
            # edit_contact = contact.Contact(first_name = edit_first_name, last_name =edit_last_name, mobile_number = edit_mobile_number, email = edit_email)

        if choice == 4:
            #delete a contact
            delete_contact = raw_input("which contact do you want to remove")
            print delete_contact(contact)


        if choice == 5:
            #exit the program
            exit_done()
            break

 



if __name__ == '__main__':
    main()