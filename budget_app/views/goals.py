import tkinter as tk
from tkinter import ttk
from models.goal import Goal
from utils.db import create_connection  # Ajoutez cette ligne

class Goals(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Gestion des Objectifs Financiers")
        self.label.pack(pady=10, padx=10)

        self.description_entry = tk.Entry(self)
        self.description_entry.pack()

        self.target_amount_entry = tk.Entry(self)
        self.target_amount_entry.pack()

        self.current_amount_entry = tk.Entry(self)
        self.current_amount_entry.pack()

        self.add_button = tk.Button(self, text="Ajouter Objectif", command=self.add_goal)
        self.add_button.pack()

        self.tree = ttk.Treeview(self, columns=("description", "target_amount", "current_amount"), show="headings")
        self.tree.heading("description", text="Description")
        self.tree.heading("target_amount", text="Montant Cible")
        self.tree.heading("current_amount", text="Montant Actuel")
        self.tree.pack(fill="both", expand=True)

        self.load_goals()

    def add_goal(self):
        description = self.description_entry.get()
        target_amount = float(self.target_amount_entry.get())
        current_amount = float(self.current_amount_entry.get())

        goal = Goal(description, target_amount, current_amount)
        goal.save()
        self.load_goals()

    def load_goals(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute("SELECT description, target_amount, current_amount FROM goals")
            rows = c.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
