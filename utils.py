# function to convert list to dictionary declared here
def convert_list_to_dictionary(contact_book_data):
    field_names = contact_book_data[0]
    contact_list = []

    for contact in contact_book_data[1:]:
        contact_dic = {}

        for i in range(0, len(contact)):
            contact_dic[field_names[i].lower()] = contact[i]

        contact_list.append(contact_dic)

    return contact_list

# function to show contact in a proper manner declared here
def show_contact(index, contact):
    print(str(index) + '.')
    print(f'Name: {contact['name']}')
    print(f'Phone Number: {contact['phone']}')
    print(f'Email: {contact['email']}')
    print(f'Address: {contact['address']}')
    print('\n')