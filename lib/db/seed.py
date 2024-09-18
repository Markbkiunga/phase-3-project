#!/usr/bin/env python
from models import Category, Expense, Income, User


def seed():
    # Drop existing tables
    print("Dropping tables (if they exist)...")
    User.drop_table()
    Category.drop_table()
    Income.drop_table()
    Expense.drop_table()

    # Create tables
    print("Creating tables...")
    User.create_table()
    Category.create_table()
    Income.create_table()
    Expense.create_table()

    # Seed Users
    print("Seeding users...")
    user1 = User.create(name="Alice")
    user2 = User.create(name="Bob")
    user3 = User.create(name="Charlie")

    # Seed Categories
    print("Seeding categories...")
    category1 = Category.create(name="Food")
    category2 = Category.create(name="Transport")
    category3 = Category.create(name="Entertainment")
    category4 = Category.create(name="Rent")
    category5 = Category.create(name="Healthcare")

    # Seed Incomes
    print("Seeding incomes...")
    income1 = Income.create(
        source="Salary", amount=5000.0, date="2024-08-01", user_id=user1.id
    )
    income2 = Income.create(
        source="Freelance", amount=1200.0, date="2024-08-05", user_id=user1.id
    )
    income3 = Income.create(
        source="Part-time Job", amount=1000.0, date="2024-08-10", user_id=user2.id
    )
    income4 = Income.create(
        source="Investments", amount=1500.0, date="2024-08-15", user_id=user2.id
    )
    income5 = Income.create(
        source="Salary", amount=4500.0, date="2024-08-01", user_id=user3.id
    )

    # Seed Expenses
    print("Seeding expenses...")
    expense1 = Expense.create(
        amount=300.0, date="2024-08-02", category_id=category1.id, user_id=user1.id
    )  # Alice - Food
    expense2 = Expense.create(
        amount=50.0, date="2024-08-03", category_id=category2.id, user_id=user1.id
    )  # Alice - Transport
    expense3 = Expense.create(
        amount=1500.0, date="2024-08-05", category_id=category4.id, user_id=user1.id
    )  # Alice - Rent
    expense4 = Expense.create(
        amount=120.0, date="2024-08-06", category_id=category5.id, user_id=user1.id
    )  # Alice - Healthcare

    expense5 = Expense.create(
        amount=80.0, date="2024-08-02", category_id=category1.id, user_id=user2.id
    )  # Bob - Food
    expense6 = Expense.create(
        amount=60.0, date="2024-08-04", category_id=category2.id, user_id=user2.id
    )  # Bob - Transport
    expense7 = Expense.create(
        amount=1100.0, date="2024-08-08", category_id=category4.id, user_id=user2.id
    )  # Bob - Rent
    expense8 = Expense.create(
        amount=75.0, date="2024-08-09", category_id=category3.id, user_id=user2.id
    )  # Bob - Entertainment

    expense9 = Expense.create(
        amount=500.0, date="2024-08-03", category_id=category1.id, user_id=user3.id
    )  # Charlie - Food
    expense10 = Expense.create(
        amount=100.0, date="2024-08-06", category_id=category5.id, user_id=user3.id
    )  # Charlie - Healthcare
    expense11 = Expense.create(
        amount=1300.0, date="2024-08-10", category_id=category4.id, user_id=user3.id
    )  # Charlie - Rent
    expense12 = Expense.create(
        amount=95.0, date="2024-08-12", category_id=category3.id, user_id=user3.id
    )  # Charlie - Entertainment

    print("Seeding complete.")


if __name__ == "__main__":
    seed()
