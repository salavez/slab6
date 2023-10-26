# Soch Alavez

# Function to encode 8-digit password
def encode(password):
    encoded_password = ""
    for char in password: # Shift by 3
        shifted_pass = (int(char) + 3) % 10
        encoded_password += str(shifted_pass)
    return encoded_password

#  Menu
def menu_options():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
# function for decoding password
def decode(password):  # Pulled code and merged
    # make string
    decoded_password = ''
    # for loop to make integer, subtract 3, make string, and add to empty string
    for i in password:
        i = int(i)
        i -= 3
        i = str(i)
        decoded_password += i
    return decoded_password


# Main function
if __name__ == '__main__':
    continue_loop = True
    while continue_loop:
        menu_options()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif menu_option == 2:  # Adding elif condition for option 2
             # store decoded password
             decoded_password = decode(encoded_password)
             # print statement
             print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')
        elif menu_option == 3:
             continue_loop = False  # Terminates Program
