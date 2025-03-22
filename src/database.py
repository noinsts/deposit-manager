import sqlite3

DB_NAME = "deposits.db"


def init_db():
    """Створює базу, якщо її нема"""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deposits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                bank_name TEXT NOT NULL, 
                interest_3_6 REAL NOT NULL,
                interest_6_9 REAL NOT NULL,
                interest_9_12 REAL NOT NULL,
                interest_18 REAL NOT NULL,
                interest_24 REAL NOT NULL
            )
        """)
        conn.commit()


def add_deposit(name, bank_name, interest_3_6, interest_6_9, interest_9_12, interest_18, interest_24,):
    """Додає депозит до бази даних"""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO deposits (
                name, bank_name, interest_3_6, interest_6_9, interest_9_12, interest_18, interest_24) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, bank_name, interest_3_6, interest_6_9, interest_9_12, interest_18, interest_24,))
        conn.commit()


def get_deposits():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM deposits")
        deposits = cursor.fetchall()
    return deposits


def remove_deposite(name, bank_name):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM deposits WHERE name = ? AND bank_name = ?", (name, bank_name))
        conn.commit()
    return cursor.rowcount


def names_deposit():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM deposits")
        names = cursor.fetchall()
    return names


def bank_name_deposit(name):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT bank_name FROM deposits WHERE name = ?", (name, ))
        bank_names = cursor.fetchall()
    return bank_names


def get_need_depo(name, bank_name):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT interest_3_6, interest_6_9, interest_9_12, "
                       "interest_18, interest_24 FROM deposits WHERE name = ? and bank_name = ?", (name, bank_name))
        row = cursor.fetchone()

    if row:
        keys = ["interest_3_6", "interest_6_9", "interest_9_12", "interest_18", "interest_24"]
        return dict(zip(keys, row))

    return None


def update_deposit(name, bank_name, updated_data):
    """Оновлює депозит у базі"""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE deposits 
            SET interest_3_6 = ?, interest_6_9 = ?, interest_9_12 = ?, 
                interest_18 = ?, interest_24 = ? WHERE name = ? AND bank_name = ?
        """, (*updated_data.values(), name, bank_name))
        conn.commit()


def percent(bank_name, interest_column):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT {interest_column}, name FROM deposits WHERE bank_name = ?", (bank_name, ))
        result = cursor.fetchall()
    return result
