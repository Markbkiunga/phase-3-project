#!/usr/bin/env python
from helpers import (
    exit_program,
    list_categories,
    list_expenses,
    list_incomes,
    list_users,
    find_category_by_id,
    find_expense_by_id,
    find_income_by_id,
    find_user_by_id,
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
        elif choice == "5":
            find_category_by_id()
        elif choice == "6":
            find_expense_by_id()
        elif choice == "7":
            find_income_by_id()
        elif choice == "8":
            find_user_by_id()


def menu():
    print("Please select an option:")
    print("0 - Exit the program")
    print("1 - List all categories")
    print("2 - List all expenses")
    print("3 - List all incomes")
    print("4 - List all users")
    print("5 - Find a category by ID")
    print("6 - Find an expense by ID")
    print("7 - Find an income by ID")
    print("8 - Find a user by ID")


if __name__ == "__main__":
    main()
