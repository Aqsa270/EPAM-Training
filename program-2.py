"""Basic Python Programs
Run this file with: python program.py
Choose a program from the menu.
"""

def show_menu():
    print("\n--- BASIC PYTHON PROGRAMS ---")
    print("1. Add two numbers")
    print("2. Check even or odd")
    print("3. Find largest of three numbers")
    print("4. Factorial of a number")
    print("5. Multiplication table")
    print("6. Fibonacci series")
    print("7. Check prime number")
    print("8. Reverse a string")
    print("9. Check palindrome")
    print("10. Sum of list elements")
    print("0. Exit")


def add_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum =", a + b)


def even_or_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def largest_of_three():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    print("Largest =", max(a, b, c))


def factorial():
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return
    result = 1
    for value in range(1, number + 1):
        result *= value
    print("Factorial =", result)


def multiplication_table():
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


def fibonacci_series():
    terms = int(input("How many terms? "))
    if terms < 0:
        print("Enter a non-negative number.")
        return
    first, second = 0, 1
    for _ in range(terms):
        print(first, end=" ")
        first, second = second, first + second
    print()


def prime_number():
    number = int(input("Enter an integer: "))
    if number < 2:
        print("Not a prime number")
        return
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            print("Not a prime number")
            return
    print("Prime number")


def reverse_string():
    text = input("Enter a string: ")
    print("Reversed =", text[::-1])


def palindrome():
    text = input("Enter a word or phrase: ")
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    if cleaned == cleaned[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


def sum_of_list():
    numbers = input("Enter numbers separated by spaces: ").split()
    values = [float(number) for number in numbers]
    print("Sum =", sum(values))


PROGRAMS = {
    "1": add_two_numbers,
    "2": even_or_odd,
    "3": largest_of_three,
    "4": factorial,
    "5": multiplication_table,
    "6": fibonacci_series,
    "7": prime_number,
    "8": reverse_string,
    "9": palindrome,
    "10": sum_of_list,
}


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose a program: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        program = PROGRAMS.get(choice)
        if program:
            try:
                program()
            except ValueError:
                print("Invalid input. Please enter the correct type of value.")
        else:
            print("Invalid choice. Please select from the menu.")
