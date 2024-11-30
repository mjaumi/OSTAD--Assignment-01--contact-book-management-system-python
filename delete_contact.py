from read_contact_book import read_contact_book
from save_contact_book import save_contact_book


# function to delete contact from CSV file declared here
def delete_contact(contact_book_list):
    print('\n---------------------------')
    print('DELETE CONTACT')
    print('---------------------------\n')

    phone = input("Enter The Contact's Phone Number You Want To Delete: ")

    for contact in contact_book_list:
        if contact['phone'] == phone:
            contact_book_list.remove(contact)
            save_contact_book(contact_book_list)
            print('\nContact Deleted Successfully!!\n')
            return

    print('\nContact With The Given Phone Number Does Not Exist!!\n')