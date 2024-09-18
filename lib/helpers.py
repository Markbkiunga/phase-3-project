from db.models import Category, Expense, Income, User


def exit_program():
    print("Goodbye!")
    print("Made By Mark Brian♡")
    exit()


def list_categories():
    categories = Category.get_all()
    for category in categories:
        print(f"{category.id}. {category}")


def list_expenses():
    expenses = Expense.get_all()
    for expense in expenses:
        print(f"{expense.id}. {expense}")


def list_incomes():
    incomes = Income.get_all()
    for income in incomes:
        print(f"{income.id}. {income}")


def list_users():
    users = User.get_all()
    for user in users:
        print(f"{user.id}. {user}")


def find_category_by_id():
    id = int(input("Enter category id: "))
    category = Category.find_by_id(id)
    (
        print(f"\nCategory Found! \n >{category}", "\n")
        if category
        else print(f"Category {id} not found")
    )


def find_expense_by_id():
    id = int(input("Enter expense id: "))
    expense = Expense.find_by_id(id)
    (
        print(f"\nExpense Found! \n >{expense}", "\n")
        if expense
        else print(f"Expense {id} not found")
    )


def find_income_by_id():
    id = int(input("Enter income id: "))
    income = Income.find_by_id(id)
    (
        print(f"\nIncome Found! \n >{income}", "\n")
        if income
        else print(f"Income {id} not found")
    )


def find_user_by_id():
    id = int(input("Enter user id: "))
    user = User.find_by_id(id)
    (
        print(f"\nUser Found! \n >{user}", "\n")
        if user
        else print(f"User {id} not found")
    )


def create_category():
    name = input("Enter the category's name: ")
    try:
        category = Category.create(name)
        print(f"Success: {category} created")
    except Exception as exc:
        print("Error creating category: ", exc)


def create_expense():
    amount = float(input("Enter the expense's amount: "))
    date = input("Enter the expense's date: ")
    category_id = int(input("Enter the expense's category_id: "))
    user_id = int(input("Enter the expense's user_id: "))
    try:
        expense = Expense.create(amount, date, category_id, user_id)
        print(f"Success: {expense} created")
    except Exception as exc:
        print("Error creating expense: ", exc)


def create_income():
    source = input("Enter the income's source: ")
    amount = float(input("Enter the expense's amount: "))
    date = input("Enter the expense's date: ")
    user_id = int(input("Enter the expense's user_id: "))
    try:
        income = Income.create(source, amount, date, user_id)
        print(f"Success: {income} created")
    except Exception as exc:
        print("Error creating income: ", exc)


def create_user():
    name = input("Enter the user's name: ")
    try:
        user = User.create(name)
        print(f"Success: {user} created")
    except Exception as exc:
        print("Error creating user: ", exc)


def update_category():
    id = input("Enter the category's id: ")
    if category := Category.find_by_id(id):
        try:
            name = input("Enter the category's new name: ")
            category.name = name
            category.update()
            print(f"Success: Category updated to {category}")
        except Exception as exc:
            print("Error updating category: ", exc)
    else:
        print(f"Category {id} not found")


def update_expense():
    id = input("Enter the expense's id: ")
    if expense := Expense.find_by_id(id):
        try:
            amount = float(input("Enter the expense's new amount: "))
            expense.amount = amount
            date = input("Enter the expense's new date: ")
            expense.date = date
            category_id = int(input("Enter the expense's new category_id: "))
            expense.category_id = category_id
            user_id = int(input("Enter the new expense's user_id: "))
            expense.user_id = user_id
            expense.update()
            print(f"Success: Expense updated to {expense}")
        except Exception as exc:
            print("Error updating expense: ", exc)
    else:
        print(f"Expense {id} not found")


def update_income():
    id = input("Enter the income's id: ")
    if income := Income.find_by_id(id):
        try:
            source = input("Enter the income's new source: ")
            income.source = source
            amount = float(input("Enter the income's new amount: "))
            income.amount = amount
            date = input("Enter the income's new date: ")
            income.date = date
            user_id = int(input("Enter the new income's user_id: "))
            income.user_id = user_id
            income.update()
            print(f"Success: Income updated to {income}")
        except Exception as exc:
            print("Error updating income: ", exc)
    else:
        print(f"Income {id} not found")


def update_user():
    id = input("Enter the user's id: ")
    if user := User.find_by_id(id):
        try:
            name = input("Enter the user's new name: ")
            user.name = name
            user.update()
            print(f"Success: User updated to {user}")
        except Exception as exc:
            print("Error updating user: ", exc)
    else:
        print(f"User {id} not found")


def delete_category():
    id = input("Enter the category's id: ")
    if category := Category.find_by_id(id):
        try:
            category.delete()
            print(f"Success: Category {id} deleted")
        except Exception as exc:
            print("Error deleting category: ", exc)
    else:
        print(f"Category {id} not found")


def delete_expense():
    id = input("Enter the expense's id: ")
    if expense := Expense.find_by_id(id):
        try:
            expense.delete()
            print(f"Success: Expense {id} deleted")
        except Exception as exc:
            print("Error deleting expense: ", exc)
    else:
        print(f"Expense {id} not found")


def delete_income():
    id = input("Enter the income's id: ")
    if income := Income.find_by_id(id):
        try:
            income.delete()
            print(f"Success: Income {id} deleted")
        except Exception as exc:
            print("Error deleting income: ", exc)
    else:
        print(f"Income {id} not found")


def delete_user():
    id = input("Enter the user's id: ")
    if user := User.find_by_id(id):
        try:
            user.delete()
            print(f"Success: User {id} deleted")
        except Exception as exc:
            print("Error deleting user: ", exc)
    else:
        print(f"User {id} not found")
