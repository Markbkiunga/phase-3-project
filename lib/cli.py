#!/usr/bin/env python
from helpers import (
    exit_program,
    list_categories,
    list_expenses,
    list_incomes,
    list_users,
)


def main():
    while True:
        menu()
        choice = input("=> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            list_incomes()
        elif choice == "4":
            list_users()


def menu():
    print("Please select an option:")
    print("0 - Exit the program")
    print("1 - List all categories")
    print("2 - List all expenses")
    print("3 - List all incomes")
    print("4 - List all users")


if __name__ == "__main__":
    main()
