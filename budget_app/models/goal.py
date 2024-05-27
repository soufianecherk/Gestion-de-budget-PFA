from utils.db import create_connection

class Goal:
    def __init__(self, description, target_amount, current_amount=0):
        self.description = description
        self.target_amount = target_amount
        self.current_amount = current_amount

    def save(self):
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute('INSERT INTO goals (description, target_amount, current_amount) VALUES (?, ?, ?)', 
                      (self.description, self.target_amount, self.current_amount))
            conn.commit()

    @staticmethod
    def get_all():
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute('SELECT * FROM goals')
            return c.fetchall()
