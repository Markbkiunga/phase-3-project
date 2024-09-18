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
