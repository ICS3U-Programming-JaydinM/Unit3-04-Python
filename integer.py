#!/usr/bin/env python3

# Made By Jaydin Madore
# Made on Oct. 12, 2022
# This program checks if an integer is positive, negative, or neither.


def main():
    # Gets the user's integer
    integer = int(input("Enter an integer: "))

    # Code executed if the integer is greater than zero.
    if integer > 0:
        print(f"{integer} is positive.")

    # Code executed if the integer is less than zero.
    elif integer < 0:
        print(f"{integer} is negative.")

    # Code executed if the integer is zero.
    else:
        print("Your integer is not negative or positive (0).")


if __name__ == "__main__":
    main()