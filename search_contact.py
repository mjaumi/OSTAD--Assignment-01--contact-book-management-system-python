from read_contact_book import read_contact_book
from utils import show_contact

# function to search contacts from the CSV file declared here
def search_contact(contact_book_list):
    print('\n---------------------------')
    print('SEARCH CONTACTS')
    print('---------------------------\n')

    phone = input("Enter The Contact's Phone Number You Want To Search: ")

    for index, contact in enumerate(contact_book_list, 1):
        if contact['phone'] == phone:
            print('\nContact Found!!\n')
            show_contact(index, contact)
            return

    print('\nNo Contacts Found!!\n')