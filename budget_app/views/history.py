import tkinter as tk
from tkinter import ttk
from utils.db import create_connection

class History(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Historique des Transactions")
        self.label.pack(pady=10, padx=10)

        self.tree = ttk.Treeview(self, columns=("date", "category", "subcategory", "amount", "note"), show="headings")
        self.tree.heading("date", text="Date")
        self.tree.heading("category", text="Catégorie")
        self.tree.heading("subcategory", text="Sous-catégorie")
        self.tree.heading("amount", text="Montant")
        self.tree.heading("note", text="Note")
        self.tree.pack(fill="both", expand=True)

        self.load_history()

    # Ajout d'un bouton pour revenir au tableau de bord
        self.back_button = tk.Button(self, text="Retour au Tableau de Bord", 
                                     command=lambda: self.controller.show_frame("Dashboard"))
        self.back_button.pack(pady=5)

    def load_history(self):
        conn = create_connection()
        with conn:
            c = conn.cursor()
            c.execute("SELECT date, category, subcategory, amount, note FROM transactions")
            rows = c.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
