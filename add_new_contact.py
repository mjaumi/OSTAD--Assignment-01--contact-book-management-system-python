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

    for contact in contact_book_list:
        if contact['phone'] == phone_no:
            print('\nA Contact With The Similar Phone Number Already Exists!!\n')
            return

    # providing name input validation here
    if not name.isalpha():
        print("\nContact's Name Must Be A String!!\n")

    # providing phone number input validation here
    if not phone_no.isdigit():
        print("\nContact's Phone Number Must Be An Integer!!\n")

    # providing email input validation here
    if not '@' in email.lower() or not email.lower()[-4:] in '.com.org.edu.gov.net':
        print('\nInvalid Email!!\n')

    if not len(address):
        print('\nAddress Is Required!!\n')

    # returning from the function if any of the validation failed here
    if (not name.isalpha() or
            not phone_no.isdigit() or
            not '@' in email.lower() or
            not email.lower()[-4:] in '.com.org.edu.gov.net' or
            not len(address)):
        return

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

