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

    @classmethod
    def instance_from_db(cls, row):
        """Return a Category object having the attribute values from the table row."""
        category = cls.all.get(row[0])
        if category:
            category.name = row[1]
        else:
            category = cls(row[1])
            category.id = row[0]
            cls.all[category.id] = category
        return category

    @classmethod
    def get_all(cls):
        """Return a list containing a Category object per row in the table"""
        sql = """
            SELECT *
            FROM categories
        """

        rows = cursor.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Category object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM categories
            WHERE id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None


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

    @classmethod
    def instance_from_db(cls, row):
        """Return an Expense object having the attribute values from the table row."""
        expense = cls.all.get(row[0])
        if expense:
            expense.amount = row[1]
            expense.date = row[2]
            expense.category_id = row[3]
            expense.user_id = row[4]
        else:
            expense = cls(row[1], row[2], row[3], row[4])
            expense.id = row[0]
            cls.all[expense.id] = expense
        return expense

    @classmethod
    def get_all(cls):
        """Return a list containing a Expense object per row in the table"""
        sql = """
            SELECT *
            FROM expenses
        """

        rows = cursor.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Expense object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM expenses
            WHERE id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None


class Income:
    all = {}

    def __init__(self, source, amount, date, user_id):
        self.source = source
        self.amount = amount
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return f"Income of {self.amount} on {self.date} sourced from {self.source} for user {self.user_id}"

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

    @classmethod
    def instance_from_db(cls, row):
        """Return an Expense object having the attribute values from the table row."""
        income = cls.all.get(row[0])
        if income:
            income.source = row[1]
            income.amount = row[2]
            income.date = row[3]
            income.user_id = row[4]
        else:
            income = cls(row[1], row[2], row[3], row[4])
            income.id = row[0]
            cls.all[income.id] = income
        return income

    @classmethod
    def get_all(cls):
        """Return a list containing a Income object per row in the table"""
        sql = """
            SELECT *
            FROM incomes
        """

        rows = cursor.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Income object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM incomes
            WHERE id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None


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

    @classmethod
    def instance_from_db(cls, row):
        """Return a User object having the attribute values from the table row."""
        user = cls.all.get(row[0])
        if user:
            user.name = row[1]
        else:
            user = cls(row[1])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        """Return a list containing a User object per row in the table"""
        sql = """
            SELECT *
            FROM users
        """

        rows = cursor.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return User object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
