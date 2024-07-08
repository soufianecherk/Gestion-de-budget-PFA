import tkinter as tk
from tkinter import ttk
import sqlite3
from utils.db import create_connection

class History(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Historique", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=20)

        # Création du Treeview
        self.history_tree = ttk.Treeview(self, columns=("ID", "Date", "Catégorie", "Sous-catégorie", "Montant", "Note"), show='headings')
        self.history_tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Définition des colonnes
        self.history_tree.heading("ID", text="ID")
        self.history_tree.heading("Date", text="Date")
        self.history_tree.heading("Catégorie", text="Catégorie")
        self.history_tree.heading("Sous-catégorie", text="Sous-catégorie")
        self.history_tree.heading("Montant", text="Montant")
        self.history_tree.heading("Note", text="Note")

        # Définir les largeurs de colonnes
        self.history_tree.column("ID", width=50, anchor='center')
        self.history_tree.column("Date", width=100, anchor='center')
        self.history_tree.column("Catégorie", width=100, anchor='center')
        self.history_tree.column("Sous-catégorie", width=100, anchor='center')
        self.history_tree.column("Montant", width=80, anchor='center')
        self.history_tree.column("Note", width=150, anchor='center')

        self.load_history()
    
        # Ajout d'un bouton pour revenir au tableau de bord
        btn_font = ("Helvetica", 12, "bold")
        self.back_button = tk.Button(self, text="Retour au Tableau de Bord", 
                                     command=lambda: self.controller.show_frame("Dashboard"), font=btn_font, bg="#2196F3", fg="white")
        self.back_button.pack(pady=20)

    def load_history(self):
        conn = create_connection("budget.db")
        if conn is not None:
            try:
                c = conn.cursor()
                c.execute("SELECT * FROM transactions")
                rows = c.fetchall()
                for row in rows:
                    self.history_tree.insert("", "end", values=row)
            except sqlite3.Error as e:
                print(e)
            finally:
                conn.close()
        else:
            print("Error! Cannot create the database connection.")
