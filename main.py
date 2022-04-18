from menu_display import display_menu
from n_and_phi_generator import calculate_n_and_phi
from public_key_generator import generate_public_key
from private_key_generator import generate_private_key
from encrypter_decrypter import encrypt, decrypt

# This is where it all comes together.
# Takes input from console, encrypts and decrypts messages (represented by numbers)
# Using private and public keys selected.

# Some useful four digit prime numbers:
# 8999, 1949, 9467, 2003, 3347

def main():

    keys_generated = False 
    choice = display_menu()

    while choice != 'X':

        if choice == 'G':
            n, phi = calculate_n_and_phi()
            public_key_1, n = generate_public_key(n, phi)
            private_key_1, n = generate_private_key(public_key_1, n, phi)
            keys_generated = True 
            print('Keys have been generated') 
            print('Public key: (', public_key_1, ', ',  n, ')', sep='')
            choice_priv_key = str(input("Please type 'Yes' to access the private key \n"))
            if choice_priv_key.lower() == "yes":
                print('Private key: (', private_key_1, ', ', n, ')', '\n', sep='')

        elif choice == 'E':
            if not keys_generated: 
                print('You need to generate the keys before encryption\n') 
            else: 
                x = int(input('Enter the message to be encrypted: '))
                public_key_input = int(input("Please enter the first element of public key: "))
                y = encrypt(x, public_key_input, n)
                print(x, 'is encrypted as', y, '\n')

        elif choice == 'D':
            if not keys_generated: 
                print('You need to generate the keys before decryption', '\n') 
            else: 
                y = int(input('Enter the message to be decrypted: '))
                private_key_input = int(input("Please enter the first element of private key: "))
                x = decrypt(y, private_key_input, n)
                print(y, 'is decrypted as', x, '\n')
        choice = display_menu()


if __name__ == "__main__":
    main()
