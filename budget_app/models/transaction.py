import sqlite3

class Transaction:
    def __init__(self, id, date, category, subcategory, amount, note):
        self.id = id
        self.date = date
        self.category = category
        self.subcategory = subcategory
        self.amount = amount
        self.note = note

    @classmethod
    def from_db_row(cls, row):
        return cls(*row)

    def save(self):
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO transactions (date, category, subcategory, amount, note) VALUES (?, ?, ?, ?, ?)',
                       (self.date, self.category, self.subcategory, self.amount, self.note))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE transactions SET date = ?, category = ?, subcategory = ?, amount = ?, note = ? WHERE id = ?',
                       (self.date, self.category, self.subcategory, self.amount, self.note, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM transactions WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
