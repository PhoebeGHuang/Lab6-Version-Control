#PhoebeHuang
def encode(password):
    encoded = ""
    for element in password:
        digit = int(element)
        new_digit = (digit + 3) % 10  # Add 3 to each digit, if sum > 10, will only take ones digit
        encoded += str(new_digit)

    return encoded

def decode(password):
    original_password = ''
    for value in password:
        new_value = (int(value) - 3) % 10  #shifts each digit down by 3 & wraps
        original_password += str(new_value)

    return original_password


while True:  # repeat until loop exited by user
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    menu_option = input("Please enter an option: ")

    if menu_option == "1":
        password = input("Please enter your password to encode: ")
        encoded = encode(password)
        print("Your password has been encoded and stored!")
        print()

    if menu_option == "2":
        decoded = decode(encoded)
        print(f"The encoded password is {encoded}, and the original password is {decoded}")
        print()

    if menu_option == "3":
        break
