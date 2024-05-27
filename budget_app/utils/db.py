import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('budget.db')
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables():
    conn = create_connection()
    with conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                date TEXT,
                category TEXT,
                subcategory TEXT,
                amount REAL,
                note TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT,
                subcategories TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY,
                description TEXT,
                target_amount REAL,
                current_amount REAL
            )
        ''')

if __name__ == '__main__':
    create_tables()
