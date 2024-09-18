import sqlite3

conn = sqlite3.connect("finance_manager.db")
cursor = conn.cursor()


class Category:
    all = {}

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Category {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Category Name must be a string")
        self._name = name

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Category instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Category instances"""
        sql = """
            DROP TABLE IF EXISTS categories;
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        """Insert a new row with the name values of the current Category object.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
                INSERT INTO categories (name)
                VALUES (?)
        """

        cursor.execute(sql, (self.name,))
        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Category instance."""
        sql = """
            UPDATE categories
            SET name = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.id))
        conn.commit()

    def delete(self):
        """Delete the table row corresponding to the current Category instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM categories
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name):
        """Initialize a new Employee instance and save the object to the database"""
        category = cls(name)
        category.save()
        return category


class Expense:
    all = {}

    def __init__(self, amount, date, category_id, user_id):
        self.amount = amount
        self.date = date
        self.category_id = category_id
        self.user_id = user_id

    def __repr__(self):
        return f"{self.amount} on {self.date} in category {self.category_id} for user {self.user_id}"

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if not isinstance(amount, (float, int)) or amount <= 0:
            raise ValueError("Amount must be a positive integer or float")
        self._amount = float(amount)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise ValueError("Date must be a string")
        self._date = date

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if not isinstance(category_id, int):
            raise ValueError("Category ID must be an integer")
        self._category_id = category_id

    @property
    def user_id(self):
        return self._user_id

    def user_id(self, user_id):
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer")
        self._user_id = user_id

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Expense instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            amount FLOAT NOT NULL,
            date TEXT NOT NULL,
            category_id INTEGER,
            user_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Expense instances"""
        sql = """
            DROP TABLE IF EXISTS expenses;
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        """Insert a new row with the amount, date, category_id and user_id values of the current Expense object.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
                INSERT INTO expenses (amount, date, category_id, user_id)
                VALUES (?, ?, ?, ?)
        """

        cursor.execute(sql, (self.amount, self.date, self.category_id, self.user_id))
        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Expense instance."""
        sql = """
            UPDATE expenses
            SET amount = ?, date = ?, category_id = ?, user_id = ?
            WHERE id = ?
        """
        cursor.execute(
            sql, (self.amount, self.date, self.category_id, self.user_id, self.id)
        )
        conn.commit()

    def delete(self):
        """Delete the table row corresponding to the current Expense instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM expenses
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, amount, date, category_id, user_id):
        """Initialize a new Employee instance and save the object to the database"""
        expense = cls(amount, date, category_id, user_id)
        expense.save()
        return expense


class Income:
    all = {}

    def __init__(self, source, amount, date, user_id):
        self.source = source
        self.amount = amount
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return f"Income of {self.amount} on {self.date} sourced from {self.source} for user  {self.user_id}"

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        if not isinstance(source, str):
            raise ValueError("Source must be a string")
        self._source = source

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive float or integer")
        self._amount = float(amount)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise ValueError("Date must be a string")
        self._date = date

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer")
        self._user_id = user_id

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Income instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS incomes (
            id INTEGER PRIMARY KEY,
            source TEXT NOT NULL,
            amount FLOAT NOT NULL,
            date TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Income instances"""
        sql = """
            DROP TABLE IF EXISTS incomes;
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        """Insert a new row with the amount, date, category_id and user_id values of the current Income object.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
                INSERT INTO incomes (source, amount, date, user_id)
                VALUES (?, ?, ?, ?)
        """

        cursor.execute(sql, (self.source, self.amount, self.date, self.user_id))
        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Income instance."""
        sql = """
            UPDATE incomes
            SET source = ?, amount = ?, date = ?, user_id = ?
            WHERE id = ?
        """
        cursor.execute(
            sql, (self.source, self.amount, self.date, self.user_id, self.id)
        )
        conn.commit()

    def delete(self):
        """Delete the table row corresponding to the current Income instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM incomes
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, source, amount, date, user_id):
        """Initialize a new Employee instance and save the object to the database"""
        income = cls(source, amount, date, user_id)
        income.save()
        return income


class User:
    all = {}

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
        self._name = name

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of User instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists User instances"""
        sql = """
            DROP TABLE IF EXISTS users;
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        """Insert a new row with the name value of the current User object.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
                INSERT INTO users (name)
                VALUES (?)
        """

        cursor.execute(sql, (self.name,))
        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current User instance."""
        sql = """
            UPDATE users
            SET name = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.id))
        conn.commit()

    def delete(self):
        """Delete the table row corresponding to the current User instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM users
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name):
        """Initialize a new Employee instance and save the object to the database"""
        user = cls(name)
        user.save()
        return user
