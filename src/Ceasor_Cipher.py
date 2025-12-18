import string
import sys

# Ceasor encrypt function to encrypt message with key
def ceasor_encrypt(key,message):
    # Creates the shift from the key and the remaindar of 26 (length of the alphabet)
    shift = key % 26
    # Gets the lowercase alphabet from the string libary
    alphabet = string.ascii_lowercase
    # Creates the shifted alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    # Maps the alphabet to a dictionary that allows me to shift the letters
    cipher = str.maketrans(alphabet, shifted_alphabet)
    # Makes the message to encrypt lowercase
    message_to_encrypt = message.lower()
    # Encrypts the message
    encrypted_message = message_to_encrypt.translate(cipher)
    
    # Returns the message
    return encrypted_message

# Ceasor Decrypt Function
def ceasor_decrypt(key,message):
    # Creates the shift from the key and the remaindar of 26 (length of the alphabet)
    undo_shift = 26 - (key % 26)
    # Gets the lowercase alphabet from the string libary
    alphabet = string.ascii_lowercase
    # Creates the unshifted alphabet
    deshifted_alphabet = alphabet[undo_shift:] + alphabet[:undo_shift]
    # Maps the alphabet to a dictionary that allows me to shift the letters
    reverse_cipher = str.maketrans(alphabet, deshifted_alphabet)
    # Makes the message to decrypt lowercase
    message_to_decrypt = message.lower()
    # decrypts the message
    decrypted_message = message_to_decrypt.translate(reverse_cipher)
    
    # Returns the message
    return decrypted_message

def main():
    # Program header
    print("=" * 30)
    print("Ceasor Cipher")
    
    # Loops the program while true
    while True:
        # User interface menu for showing the options a user would want to input
        print("=" * 30)
        print("User Choices: ")
        print("(1) Encryption")
        print("(2) Decryption")
        print("(3) Exit")
        print("=" * 30)
        
        # Tries to allow the user to input a number and perform a function
        try:
            # Allows the user to enter a number 
            user_choice = int(input("Input Your Choice: "))

            # Checks if the option is encrypt
            if user_choice == 1:
                # Allows the user to input a shift value
                shift_value = int(input("Please Input Shift Value: "))
                
                # Allows a user to input a message
                message = input("Please Input Your Message To Encrypt: ")
                
                # Outputs the decrypted function from the message
                print(f"Decrypted Message: {ceasor_encrypt(shift_value,message)}")
            # Checks if the option is decrypt
            elif user_choice == 2:
                # Allows the user to input a shift value
                shift_value = int(input("Please Input Shift Value: "))
                
                # Allows a user to input a message
                message = input("Please Input Your Message To Decrypt: ")
                
                # Outputs the decrypted message
                print(f"{ceasor_decrypt(shift_value,message)}")
            elif user_choice == 3:
                # Stops the program
                break
            else:
                # Prints the choice was invaild
                print("Invaild Choice:")
        # Expect exception as e
        except Exception as e:
            # Output error message
            print(f"Encountered Error: {e}")

# Starts the main function
if __name__ == "__main__":
    main()