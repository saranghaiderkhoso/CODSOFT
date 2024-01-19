# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:49:33 2024

@author: Sarang Haider Khoso
"""

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number"

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Square (Under Root)")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice not in ('1', '2', '3', '4', '5', '6'):
        print("Invalid choice")
        return

    num1 = float(input("Enter first number: "))

    if choice in ('1', '2', '3', '4') and choice != '5':
        num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        operation = "Addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "Division"
    elif choice == '5':
        result = square_root(num1)
        operation = "Square Root"
    elif choice == '6':
        result = math.pow(num1, 2)
        operation = "Square (Under Root)"
    else:
        print("Invalid choice")
        return

    print(f"{operation} result: {result}")

if __name__ == "__main__":
    calculator()
