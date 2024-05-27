from utils.db import create_connection

class Category:
    def __init__(self, name, subcategories):
        self.name = name
        self.subcategories = subcategories

    def save(self):
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute('INSERT INTO categories (name, subcategories) VALUES (?, ?)', 
                      (self.name, ','.join(self.subcategories)))
            conn.commit()

    @staticmethod
    def get_all():
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute('SELECT * FROM categories')
            return c.fetchall()
