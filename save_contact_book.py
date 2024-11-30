import csv

# function to save contacts in the CSV file declared here
def save_contact_book(contact_book):
    field_names = ['Name', 'Phone', 'Email', 'Address']

    contact_book_list = []

    # converting contact dictionary into list here
    for contact in contact_book:
        contact_book_list.append(contact.values())

    try:
        with open('contact_book.csv', 'w', newline='') as contact_book_file:
            writer = csv.writer(contact_book_file)

            writer.writerow(field_names)
            writer.writerows(contact_book_list)

        return 1

    except Exception as e:
        print('\n Something Went Wrong While Saving The Contact File!!\n')
        return 0