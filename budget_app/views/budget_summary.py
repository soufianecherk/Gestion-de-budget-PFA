import tkinter as tk
from tkinter import ttk
from utils.db import create_connection

class BudgetSummary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Résumé du Budget par Catégorie")
        self.label.pack(pady=10, padx=10)

        self.tree = ttk.Treeview(self, columns=("category", "total_budget", "total_spent", "remaining"), show="headings")
        self.tree.heading("category", text="Catégorie")
        self.tree.heading("total_budget", text="Budget Total")
        self.tree.heading("total_spent", text="Dépensé Total")
        self.tree.heading("remaining", text="Restant")
        self.tree.pack(fill="both", expand=True)

        self.load_summary()

    def load_summary(self):
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute('''
                SELECT category, SUM(amount) as total_spent
                FROM transactions
                GROUP BY category
            ''')
            rows = c.fetchall()
            for row in rows:
                # Supposez que vous avez une méthode pour obtenir le budget total par catégorie
                total_budget = 1000  # Valeur d'exemple
                total_spent = row[1]
                remaining = total_budget - total_spent
                self.tree.insert("", "end", values=(row[0], total_budget, total_spent, remaining))
