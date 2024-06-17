import sqlite3
from utils.db import create_connection

class Goal:
    def __init__(self, description="", target_amount=0.0, current_amount=0.0, goal_id=None):
        self.description = description
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.goal_id = goal_id

    def save(self):
        conn = create_connection("budget.db")
        if conn is not None:
            try:
                c = conn.cursor()
                c.execute("INSERT INTO goals (description, target_amount, current_amount) VALUES (?, ?, ?)",
                          (self.description, self.target_amount, self.current_amount))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error saving goal: {e}")
            finally:
                conn.close()

    def update(self):
        conn = create_connection("budget.db")
        if conn is not None:
            try:
                c = conn.cursor()
                c.execute("UPDATE goals SET description=?, target_amount=?, current_amount=? WHERE id=?",
                          (self.description, self.target_amount, self.current_amount, self.goal_id))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error updating goal: {e}")
            finally:
                conn.close()

    def delete(self):
        conn = create_connection("budget.db")
        if conn is not None:
            try:
                c = conn.cursor()
                c.execute("DELETE FROM goals WHERE id=?", (self.goal_id,))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error deleting goal: {e}")
            finally:
                conn.close()

    @staticmethod
    def get_all_goals():
        conn = create_connection("budget.db")
        goals = []
        if conn is not None:
            try:
                c = conn.cursor()
                c.execute("SELECT * FROM goals")
                rows = c.fetchall()
                for row in rows:
                    goals.append(Goal(row[1], row[2], row[3], row[0]))
            except sqlite3.Error as e:
                print(f"Error fetching goals: {e}")
            finally:
                conn.close()
        return goals
