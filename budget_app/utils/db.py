import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

# Fonction pour créer la base de données et la table des utilisateurs
def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Fonction pour créer la base de données et la table de budget
def create_tables():
    conn = create_connection('budget.db')
    with conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                date DATE,
                category TEXT,
                subcategory TEXT,
                amount REAL,
                note TEXT,
                total_budget REAL
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