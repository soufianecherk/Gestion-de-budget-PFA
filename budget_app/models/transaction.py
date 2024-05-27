from utils.db import create_connection

class Transaction:
    def __init__(self, date, category, subcategory, amount, note):
        self.date = date
        self.category = category
        self.subcategory = subcategory
        self.amount = amount
        self.note = note

    def save(self):
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute('INSERT INTO transactions (date, category, subcategory, amount, note) VALUES (?, ?, ?, ?, ?)', 
                      (self.date, self.category, self.subcategory, self.amount, self.note))
            conn.commit()

    @staticmethod
    def get_all():
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute('SELECT * FROM transactions')
            return c.fetchall()
