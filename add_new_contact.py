from save_new_contact import save_new_contact

# function to add new contact into the CSV file declared here
def add_new_contact():
    print('\n----------------------------------------')
    print('ADD NEW CONTACT')
    print('----------------------------------------\n')

    # Taking user inputs for new contact here
    name = input("Enter The Contact's Name: ")
    phone_no = input("Enter The Contact's Phone Number: ")
    email =  input("Enter The Contact's Email: ")
    address =  input("Enter The Contact's Address: ")

    contact = [name, phone_no, email, address]

    # Calling function to save the new contact into CSV file here
    save_new_contact(contact)

