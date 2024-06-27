import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def alter_table():
    conn = create_connection("budget.db")
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute("ALTER TABLE transactions ADD COLUMN total_budget REAL DEFAULT 0")
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

alter_table()