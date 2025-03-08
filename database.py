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