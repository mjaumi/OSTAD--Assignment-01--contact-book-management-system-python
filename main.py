contact_book = []

while True:
    print('Welcome To Contact Book Management System!!\n')
    print('0. Exit')
    print('1. Add Contact')
    print('2. View All Contacts')
    print('3. Search Contacts')
    print('3. Delete Contact')

    choice = input('\nChoose An Option: ')

    if choice == '0':
        print('\n----------------------------------------')
        print('EXITING CONTACT BOOK MANAGEMENT SYSTEM')
        print('----------------------------------------\n')

        print('Thank You For Using Contact Book Management System!!\n')
        break

    elif choice == '1':
        pass

    else:
        print('Please, Select A Valid Option!!\n')