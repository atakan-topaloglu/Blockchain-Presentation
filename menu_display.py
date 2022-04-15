# Following functions are used to display a "menu" in the console
# This will be a user interface for the encryption system we create.


def display_menu(): 
    user_input = False
    while not user_input:
        print('g or G for key generation')
        print('e or E for encryption')
        print('d or D for decryption')
        print('x or X to exit')

        choice = str(input('Please enter your choice: '))
        valid_choices = ["G", "E", "D", "X"]
        if choice.upper() not in valid_choices:
            print('** Invalid option **')
        else:
            user_input = True
    return choice.upper()

# choice3 = display_menu()
# print(choice3)
