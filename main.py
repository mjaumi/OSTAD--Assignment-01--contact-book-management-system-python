from add_new_contact import add_new_contact
from delete_contact import delete_contact
from read_contact_book import read_contact_book
from search_contact import search_contact
from utils import show_contact

# reading the contact book CSV file at the start when program runs here
contact_book_list = read_contact_book()

while True:
    print('Welcome To Contact Book Management System!!\n')
    print('0. Exit')
    print('1. Add Contact')
    print('2. View All Contacts')
    print('3. Search Contacts')
    print('4. Delete Contact')

    choice = input('\nChoose An Option: ')

    if choice == '0':
        print('\n----------------------------------------')
        print('EXITING CONTACT BOOK MANAGEMENT SYSTEM')
        print('----------------------------------------\n')

        print('Thank You For Using Contact Book Management System!!\n')
        break

    elif choice == '1':
        add_new_contact(contact_book_list)

    elif choice == '2':
        print('\n---------------------------')
        print('VIEW ALL CONTACTS')
        print('---------------------------\n')

        if len(contact_book_list):
            for index, contact in enumerate(contact_book_list, 1):
                show_contact(index, contact)
        else:
            print('No Contacts Found!!\n')

    elif choice == '3':
        search_contact(contact_book_list)

    elif choice == '4':
        delete_contact(contact_book_list)

    else:
        print('\nPlease, Select A Valid Option!!\n')