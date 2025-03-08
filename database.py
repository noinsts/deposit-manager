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
                interest_24 REAL NOT NULL,
                early_withdrawal INTEGER NOT NULL,
                interest_3_6_early REAL,
                interest_6_9_early REAL,
                interest_9_12_early REAL,
                interest_18_early REAL,
                interest_24_early REAL
            )
        """)
        conn.commit()

def add_deposit(name, bank_name, interest_3_6, interest_6_9, interest_9_12, interest_18, interest_24,
                early_withdrawal, interest_3_6_early, interest_6_9_early, interest_9_12_early,
                interest_18_early, interest_24_early):
    """Додає депозит до бази даних"""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO deposits (
                name, bank_name, interest_3_6, interest_6_9, interest_9_12, interest_18, interest_24, 
                early_withdrawal, interest_3_6_early, interest_6_9_early, interest_9_12_early, 
                interest_18_early, interest_24_early
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, bank_name, interest_3_6, interest_6_9, interest_9_12, interest_18, interest_24,
              early_withdrawal, interest_3_6_early, interest_6_9_early, interest_9_12_early,
              interest_18_early, interest_24_early))
        conn.commit()

