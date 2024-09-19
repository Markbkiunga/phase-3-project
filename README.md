# Phase-3-Project - Finance Manager CLI

The **Finance Manager CLI** is a simple, command-line-based financial management tool that allows users to manage their income, expenses, and financial categories. With the ability to list, create, update, and delete financial records, the tool provides an overview of a user's financial health, including calculating the net income.

## **Table of Contents**

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Database Models](#database-models)
- [Credits](#credits)

---

## **Features**

1. **User Management**

   - Create, update, delete, and list users.
   - View total incomes, expenses, and net income for individual users.

2. **Income Management**

   - Track sources of income (e.g., salary, freelance) with amounts and dates.
   - Create, update, and delete income records.

3. **Expense Management**

   - Track expenses categorized by type (e.g., food, rent, entertainment).
   - Create, update, and delete expense records.
   - View all expenses for a user and calculate total spending.

4. **Category Management**

   - Manage categories (e.g., Food, Transport, Rent, etc.) for expenses.
   - Create, update, and delete categories.

5. **Net Income Calculation**
   - Calculate the net income for each user by subtracting total expenses from total incomes.

---

## **Installation**

### **Prerequisites**

Ensure you have the following installed:

- Python 3.x
- SQLite3

### **Step-by-Step Instructions**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/finance-manager-cli.git
   cd finance-manager-cli
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies** (if any, or if you later add dependencies):

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the seed file to initialize the database**:
   This will create tables and insert seed data.

   ```bash
   python lib/db/seed.py
   ```

5. **Run the CLI application**:
   ```bash
   python cli.py
   ```

---

## **Usage**

Once the CLI application is running, you can interact with the finance manager using the following menu options:

```bash
Please select an option:
0 - Exit the program
1 - List all categories
2 - List all expenses
3 - List all incomes
4 - List all users
5 - Find a category by ID
6 - Find an expense by ID
7 - Find an income by ID
8 - Find a user by ID
9 - Create a new category
10 - Create a new expense
11 - Create a new income
12 - Create a new user
13 - Update a category
14 - Update an expense
15 - Update an income
16 - Update a user
17 - Delete a category
18 - Delete an expense
19 - Delete an income
20 - Delete a user
21 - List user expenses
22 - List user incomes
23 - Get a user's net income
```

Simply enter the number corresponding to the action you wish to perform.

---

## **Menu Options**

Here's an overview of what each menu option does:

1. **List All Categories**: Displays all available categories.
2. **List All Expenses**: Shows all recorded expenses.
3. **List All Incomes**: Shows all recorded incomes.
4. **List All Users**: Displays all users.
5. **Find a Category by ID**: Look up a category using its unique ID.
6. **Find an Expense by ID**: Look up an expense using its unique ID.
7. **Find an Income by ID**: Look up an income using its unique ID.
8. **Find a User by ID**: Look up a user using their unique ID.
9. **Create a New Category**: Add a new category to organize expenses.
10. **Create a New Expense**: Add a new expense.
11. **Create a New Income**: Add a new income source.
12. **Create a New User**: Add a new user.
13. **Update a Category**: Edit an existing category.
14. **Update an Expense**: Edit an existing expense.
15. **Update an Income**: Edit an existing income.
16. **Update a User**: Edit a user's name.
17. **Delete a Category**: Remove a category from the system.
18. **Delete an Expense**: Remove an expense record.
19. **Delete an Income**: Remove an income record.
20. **Delete a User**: Remove a user from the system.
21. **List User Expenses**: View all expenses for a given user.
22. **List User Incomes**: View all incomes for a given user.
23. **Get a User's Net Income**: Calculate a user's net income (total income minus total expenses).

---

## **Database Models**

- **User**: Represents a user of the system, who has incomes and expenses.
  - Attributes: `id`, `name`
- **Category**: Represents a category for organizing expenses (e.g., Food, Rent).

  - Attributes: `id`, `name`

- **Income**: Represents an income entry for a user.

  - Attributes: `id`, `source`, `amount`, `date`, `user_id`

- **Expense**: Represents an expense entry for a user.
  - Attributes: `id`, `amount`, `date`, `category_id`, `user_id`

### **Relationships**:

- Each **Income** and **Expense** is associated with a specific **User**.
- Each **Expense** is associated with a specific **Category**.

---

## **Contributing**

Feel free to submit a pull request or file an issue if you have any improvements or bug fixes.

---

## **Credits**

- **Author**: [Mark Brian](https://github.com/Markbkiunga) (Made with ♡)
