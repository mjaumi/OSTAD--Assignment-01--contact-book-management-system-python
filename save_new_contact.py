import csv

# function to save new contact into the CSV file declared here
def save_new_contact(contact):
    try:
        with open('contact_book.csv', 'a', newline='') as contact_file:
            writer = csv.writer(contact_file)
            writer.writerow(contact)

        print('\nNew Contact Added Successfully!!\n')

    except Exception as e:
        print('Something Went Wrong While Adding New Contact!!\n')