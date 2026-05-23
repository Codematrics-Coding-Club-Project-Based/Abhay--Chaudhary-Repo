 # Multi-Functional Scientific Calculator
# Author: Abhay Chaudhary
# B.Tech 2nd Year
# Date: 2026

import math

# ---------- Mathematical Operations ----------
def add_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a + b

def subtract_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a - b

def multiply_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a * b

def divide_numbers():
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# ---------- Scientific Operations ----------
def square_number():
    a = float(input("Enter number to square: "))
    return a ** 2

def square_root():
    a = float(input("Enter number to find square root: "))
    if a < 0:
        return "Error: Negative number has no real square root!"
    return math.sqrt(a)

def power_numbers():
    a = float(input("Enter base number: "))
    b = float(input("Enter exponent: "))
    return a ** b

def factorial_number():
    a = int(input("Enter number to find factorial: "))
    if a < 0:
        return "Error: Factorial of negative number not defined!"
    return math.factorial(a)

# ---------- Custom Personal Operations ----------
def combine_names():
    names = input("Enter names separated by comma: ").split(",")
    combined = " ".join([name.strip() for name in names])
    return combined

def sum_ages():
    ages = input("Enter ages separated by comma: ").split(",")
    total = sum([int(age.strip()) for age in ages])
    return total

# ---------- Main Calculator ----------
def calculator():
    print("Welcome to Multi-Functional Scientific Calculator!")
    while True:
        print("\nOptions:")
        print("1. Add numbers")
        print("2. Subtract numbers")
        print("3. Multiply numbers")
        print("4. Divide numbers")
        print("5. Square a number")
        print("6. Square root of a number")
        print("7. Power (a^b)")
        print("8. Factorial")
        print("9. Combine names")
        print("10. Sum ages")
        print("11. Exit")

        choice = input("Choose an option (1-11): ")

        if choice == "1":
            print("Result:", add_numbers())
        elif choice == "2":
            print("Result:", subtract_numbers())
        elif choice == "3":
            print("Result:", multiply_numbers())
        elif choice == "4":
            print("Result:", divide_numbers())
        elif choice == "5":
            print("Result:", square_number())
        elif choice == "6":
            print("Result:", square_root())
        elif choice == "7":
            print("Result:", power_numbers())
        elif choice == "8":
            print("Result:", factorial_number())
        elif choice == "9":
            print("Combined Names:", combine_names())
        elif choice == "10":
            print("Total Ages:", sum_ages())
        elif choice == "11":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Run the calculator
calculator()