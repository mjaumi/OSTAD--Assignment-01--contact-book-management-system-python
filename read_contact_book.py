import csv

from utils import convert_list_to_dictionary


# function to read all the contacts from the CSV file declared here
def read_contact_book():
    try:
        contact_book_data = []

        with open('contact_book.csv', 'r') as contact_file:
            reader = csv.reader(contact_file)

            for row in reader:
                contact_book_data.append(row)

        contact_list = convert_list_to_dictionary(contact_book_data)

        return  contact_list
    except Exception as e:
        print('Something Went Wrong While Reading All The Contacts!!\n')
        return []