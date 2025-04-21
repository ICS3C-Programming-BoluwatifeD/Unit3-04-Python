#!/usr/bin/env python3
# Created By: Boluwatife Dada
# created on March 11
# This program asks the user for an integer


def main():
    # Get the user_input(number)
    user_number = int(input("Enter an integer : "))

    # if the number is greater than 0, then it's positive
    if user_number > 0:
        print("The number is a positive number.")

    # if the number is less than 0, then it's positive
    elif user_number < 0:
        print("The number is a negative number.")

    # if the number is 0, then it's just zero
    else:
        print("The number is just zero!")


if __name__ == "__main__":
    main()
