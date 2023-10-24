def encode(password):
    encoded = ""
    for element in password:
        digit = int(element)
        new_digit = (digit + 3) % 10
        encoded += str(new_digit)

    return encoded

def decode(password):
    pass


while True:
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
        print(encoded)
        print()

    if menu_option == "2":
        decoded = decode(encoded)
        print(f"The encoded password is {encoded}, and the original password is {decoded}")
        print()

    if menu_option == "3":
        break
