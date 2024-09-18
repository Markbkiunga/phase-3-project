import sqlite3

conn = sqlite3.connect("finance_manager.db")
cursor = conn.cursor()


class Category:
    all = []

    def __init__(self, name):
        self.name = name
        Category.all.append(self)

    def __repr__(self):
        return f"Category {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Category Name must be a string")


class Expense:
    all = []

    def __init__(self, amount, date, category_id, user_id):
        self.amount = amount
        self.date = date
        self.category_id = category_id
        self.user_id = user_id
        Expense.all.append(self)

    def __repr__(self):
        return f"{self.amount} on {self.date} in category {self.category_id} for user {self.user_id}"

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if not isinstance(amount, (float, int)) or amount > 0:
            raise ValueError("Amount must be a float or an integer")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise ValueError("Date must be a string")

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if not isinstance(category_id, int):
            raise ValueError("Category ID must be an integer")

    @property
    def user_id(self):
        return self._user_id

    def user_id(self, user_id):
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer")


class Income:
    all = []

    def __init__(self, source, amount, date, user_id):
        self.source = source
        self.amount = amount
        self.date = date
        self.user_id = user_id
        Income.all.append(self)

    def __repr__(self):
        return f"Income of {self.amount} on {self.date} sourced from {self.source} for user  {self.user_id}"

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        if not isinstance(source, str):
            raise ValueError("Source must be a string")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if not isinstance(amount, (int, float)) or amount > 0:
            raise ValueError("Amount must be a float or an integer")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise ValueError("Date must be a string")

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer")


class User:
    all = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
