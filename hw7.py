
"""
Assignment-7
Author: Srikanth Thadigol Reddappa
Date: 08/15/2017
<<<<<<< HEAD

This python code adds, deletes, list and lookups key = Names, value = user_name in a pre-defined dictionary

"""
from sortedcontainers import SortedDict


=======
"""
from sortedcontainers import SortedDict

>>>>>>> 5a62a0d744d00273401b9a409d2924184fb9dcf4
# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

def print_menu():
<<<<<<< HEAD
    """
        This will print the menu for user input.
    """
=======
>>>>>>> 5a62a0d744d00273401b9a409d2924184fb9dcf4
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a user')
    print('5. Quit')
    print()

def user_input(u_input):
<<<<<<< HEAD
    """
        Arguments:
        u_input : passed to print statement as string for user input
    """

=======
>>>>>>> 5a62a0d744d00273401b9a409d2924184fb9dcf4
    # Take user input
    try:
        name = input(u_input+" :")
        if u_input is "name" and not name.isalpha():
            print("Your name must consist of letters only")
    # Catch Exception
    except Exception as e:
        print('Exception occurred, value:', e.value)
    # return the user input
    else:
        return name


# setup counter to store menu choice
menu_choice = 0
# display your menu
<<<<<<< HEAD

print_menu()
=======
print_menu()

>>>>>>> 5a62a0d744d00273401b9a409d2924184fb9dcf4
# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    try:
    # get menu choice from user
        menu_choice = int(input("Type in a number (1-5): "))
    # Catch Exception
    except Exception:
<<<<<<< HEAD
        print('Invalid Input, Try Again')
=======
        print('Invalid Input')
>>>>>>> 5a62a0d744d00273401b9a409d2924184fb9dcf4
    else:
        # view current entries
        if menu_choice == 1:
            print("Current Users:\n")
            for x, y in usernames.items():
                print("Name: {} \tUser Name: {} \n".format(x, y))

        # add an entry
        elif menu_choice == 2:
            print("Add User")
            name = user_input("name")
            if name not in usernames:
                username = user_input("username")
                usernames[name] = username
                print ("The user \033[1m{u_name}\033[0m and username \033[1m{u_username}\033[0m added succesfully to dict\n" .format(u_name=name,u_username=username))
            else:
                print("User already exists in dict")

        # remove an entry
        elif menu_choice == 3:
            print("Remove User")
            name = user_input("name")
            if name in usernames:
                del usernames[name]
                print(
                    "The user \033[1m{u_name}\033[0m was deleted successfully from dict\n".format(u_name=name))
            else:
                print("User is not in dict")
                # is user enters something strange, show them the menu

        # view user name
        elif menu_choice == 4:
            print("Lookup User")
            name = input("Name: ")
            if name in usernames:
                print ("The username of \033[1m{u_name}\033[0m is \033[1m{u_username}\033[0m" .format(u_name=name,u_username=usernames[name]))
            else:
                print ("User is incorrect")
                # is user enters something strange, show them the menu
        elif menu_choice != 5:
            print_menu()



