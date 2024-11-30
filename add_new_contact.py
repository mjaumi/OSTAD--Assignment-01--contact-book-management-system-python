from save_contact_book import save_contact_book

# function to add new contact into the CSV file declared here
def add_new_contact(contact_book_list):
    print('\n----------------------------------------')
    print('ADD NEW CONTACT')
    print('----------------------------------------\n')

    # Taking user inputs for new contact here
    name = input("Enter The Contact's Name: ")
    phone_no = input("Enter The Contact's Phone Number: ")
    email =  input("Enter The Contact's Email: ")
    address =  input("Enter The Contact's Address: ")

    contact = {
        'name': name,
        'phone': phone_no,
        'email': email,
        'address': address
    }

    contact_book_list.append(contact)

    # Calling function to save the new contact into CSV file here
    response = save_contact_book(contact_book_list)

    if response == 1:
        print('\nNew Contact Added Successfully!!\n')

