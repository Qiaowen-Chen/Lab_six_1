from typing import List, Any


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode_input(str_input):
    temp = list(str_input)
    for i in range(0, len(temp)):
        if int(temp[i]) + 3 >= 10:
            temp[i] = int(temp[i]) + 3 - 10
        else:
            temp[i] = int(temp[i]) + 3
    return str(temp)


def decode_input(str_input):
    temp = list(str_input)
    for i in range(0, len(temp)):
        if int(temp[i]) - 3 < 0:
            temp[i] = int(temp[i]) + 10 - 3
        else:
            temp[i] = int(temp[i]) + 3
    return str(temp)


if __name__ == "__main__":
    continue_loop = True
    result = ""
    while continue_loop:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            str_input = input("Please enter your password to encode: ")
            result = encode_input(str_input)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is{result}, and the original password is {decode_input(result)}. ")
        elif option == 3:
            continue_loop = False
