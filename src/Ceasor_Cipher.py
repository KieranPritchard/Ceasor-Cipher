import string
import sys

# Ceasor encrypt function
    
def ceasor_encrypt(key,message):
        
    shift = key % 26
    alphabet = string.ascii_lowercase
        
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    cipher = str.maketrans(alphabet, shifted_alphabet)

    message_to_encrypt = message.lower()

    encrypted_message = message_to_encrypt.translate(cipher)

    print("Encrypted Message: " + encrypted_message)

# Ceasor Decrypt Function

def ceasor_decrypt(key,message):
    undo_shift = 26 - (key % 26)
    alphabet = string.ascii_lowercase

    deshifted_alphabet = alphabet[undo_shift:] + alphabet[:undo_shift]
    reverse_cipher = str.maketrans(alphabet, deshifted_alphabet)

    message_to_decrypt = message.lower()

    decrypted_message = message_to_decrypt.translate(reverse_cipher)
    
    print("Decrypted Message: " + decrypted_message)

# Header element to display when the program is started

def header():
    print("-" * 30)
    print("Ceasor Cipher")



def main():
    header()
    while True:
        
        # User interface menu for showing the options a user would want to input
        print("-" * 30)
        print("User Choices: ")
        print("(1) Encryption")
        print("(2) Decryption")
        print("(3) Exit")
        print("-" * 30)
        
        # user input to decide which Ceasor function should be used
        user_choice = int(input("Input Your Choice: "))
        
        if user_choice == 1:
            shift_value = int(input("Please Input Shift Value: "))
            
            message = input("Please Input Your Message To Encrypt: ")
            
            ceasor_encrypt(shift_value,message)
        elif user_choice == 2:
            shift_value = int(input("Please Input Shift Value: "))
            
            message = input("Please Input Your Message To Decrypt: ")

            ceasor_decrypt(shift_value,message)
        elif user_choice == 3:
            sys.exit()
        else:
            print("Invaild Input: ")

if __name__ == "__main__":
    main()