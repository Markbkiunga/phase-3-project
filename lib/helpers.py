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
