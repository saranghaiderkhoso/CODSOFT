# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:51:06 2024

@author: Sarang Haider Khoso
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) 
                       for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Get user input for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number for the password length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
