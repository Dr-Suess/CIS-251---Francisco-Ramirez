#Programmer Name: Francisco Ramirez
#Date: March 5, 2020
#Hw 4 - Using dictionaries/Pickle

import pickle
FILE = "emails.dat"

# Constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
DISPLAY = 5
QUIT = 6

# main function
def main():
    # Declarations
    emails = load_emails()
    choice = 0

#Switch Menu
    while (choice != QUIT):
        choice = menu()

        if choice == LOOK_UP:
            _look_up(emails)
        elif choice == ADD:
            add(emails)
        elif choice == CHANGE:
            change(emails)
        elif choice == DELETE:
            delete(emails)
        elif choice == DISPLAY:
            display(emails)

    #save
    save_emails(emails)
    print('The information was saved.')
            

#------------------------------------#
#-------------METHODS-----------------#
#------------------------------------#
def menu():
    print()
    print('User Email Log')
    print('---------------------------')
    print('1. Look up email')
    print('2. Add a name/email pair')
    print('3. Change an email')
    print('4. Delete a name/email')
    print('5. Display all emails')
    print('6. Quit the program')
    print()

    # User Input
    choice = int(input('Enter your choice: '))
    
    while (choice < LOOK_UP) or (choice > QUIT):
        choice = int(input('Enter a valid choice: '))
    print()
    
    return(choice)

def load_emails():
    #Error catching
    try:
        #Open the file
        input_file = open(FILE,"rb")
        email_dictionary = pickle.load(input_file)
        input_file.close()

    except IOError:
        email_dictionary = {}
        
    return email_dictionary

def save_emails(emails):

    output_file = open(FILE, 'wb')

    #pickle the dictionary and save it.
    pickle.dump(emails, output_file)

    #close file
    output_file.close()


def _look_up(emails):
    name = input('Enter a name: ')
    print(emails.get(name,(name + ' not found.')))


def add(emails):
    name = input('Enter a name: ')
    address = input('Enter an email: ')
    if name not in emails:
        emails[name] = address
    else:
        print('That entry already exists.')

def change(emails):
    name = input('Enter a name: ')

    if name in emails:
        address = input('Enter the new email: ')
        emails[name] = address
        
    else:
        print('That name is not found.')


def delete(emails):
    name = input('Enter a name: ')

    if name in emails:
        del emails[name]
    else:
        print('That name is not found.')

def display(emails):
    print("Email log.")
    print("-------------------")
    for key in emails:
        print(key, emails[key])

# Call the main function.
main()

    
