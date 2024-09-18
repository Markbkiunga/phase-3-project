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
    create_category,
    create_expense,
    create_income,
    create_user,
    update_category,
    update_expense,
    update_income,
    update_user,
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
        elif choice == "9":
            create_category()
        elif choice == "10":
            create_expense()
        elif choice == "11":
            create_income()
        elif choice == "12":
            create_user()
        elif choice == "13":
            update_category()
        elif choice == "14":
            update_expense()
        elif choice == "15":
            update_income()
        elif choice == "16":
            update_user()


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
    print("9 - Create a new category")
    print("10 - Create a new expense")
    print("11 - Create a new income")
    print("12 - Create a new user")
    print("13 - Update a category")
    print("14 - Update an expense")
    print("15 - Update an income")
    print("16 - Update a user")


if __name__ == "__main__":
    main()
