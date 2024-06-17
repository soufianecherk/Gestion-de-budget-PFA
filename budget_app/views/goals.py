import tkinter as tk
from tkinter import ttk
from models.goal import Goal
import sqlite3
from utils.db import create_connection 

class Goals(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Gestion des Objectifs Financiers", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=15)

        # Champs d'entrée pour les objectifs
        self.description_entry = tk.Entry(self, width=30)
        self.description_entry.pack(pady=5)
        self.description_entry.insert(0, "Description de l'objectif")

        self.target_amount_entry = tk.Entry(self, width=30)
        self.target_amount_entry.pack(pady=5)
        self.target_amount_entry.insert(0, "Montant Cible")

        self.current_amount_entry = tk.Entry(self, width=30)
        self.current_amount_entry.pack(pady=5)
        self.current_amount_entry.insert(0, "Montant Actuel")

        # Boutons pour ajouter, modifier, supprimer et effacer
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Ajouter Objectif", command=self.add_goal)
        self.add_button.grid(row=0, column=0, padx=5, pady=3)

        self.update_button = tk.Button(button_frame, text="Modifier Objectif", command=self.update_goal)
        self.update_button.grid(row=0, column=1, padx=5, pady=3)

        self.delete_button = tk.Button(button_frame, text="Supprimer Objectif", command=self.delete_goal)
        self.delete_button.grid(row=0, column=2, padx=5, pady=3)

        self.clear_button = tk.Button(button_frame, text="Effacer", command=self.clear_fields)
        self.clear_button.grid(row=0, column=3, padx=5, pady=3)

        # Création du Treeview
        self.tree = ttk.Treeview(self, columns=("id", "description", "target_amount", "current_amount"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("description", text="Description")
        self.tree.heading("target_amount", text="Montant Cible")
        self.tree.heading("current_amount", text="Montant Actuel")
        self.tree.pack(fill="both", expand=True, pady=17)

        # Définir les largeurs de colonnes
        self.tree.column("id", width=30, anchor='center')
        self.tree.column("description", width=200, anchor='center')
        self.tree.column("target_amount", width=100, anchor='center')
        self.tree.column("current_amount", width=100, anchor='center')

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.load_goals()

        # Ajout d'un bouton pour revenir au tableau de bord
        self.back_button = tk.Button(self, text="Retour au Tableau de Bord", 
                                     command=lambda: self.controller.show_frame("Dashboard"))
        self.back_button.pack(pady=5)

    def add_goal(self):
        description = self.description_entry.get()
        target_amount = float(self.target_amount_entry.get())
        current_amount = float(self.current_amount_entry.get())

        goal = Goal(description, target_amount, current_amount)
        goal.save()
        self.load_goals()

    def update_goal(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item = self.tree.item(selected_item)
        goal_id = item['values'][0]

        description = self.description_entry.get()
        target_amount = float(self.target_amount_entry.get())
        current_amount = float(self.current_amount_entry.get())

        goal = Goal(description, target_amount, current_amount, goal_id)
        goal.update()
        self.load_goals()

    def delete_goal(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item = self.tree.item(selected_item)
        goal_id = item['values'][0]

        goal = Goal(goal_id=goal_id)
        goal.delete()
        self.load_goals()

    def clear_fields(self):
        self.description_entry.delete(0, tk.END)
        self.target_amount_entry.delete(0, tk.END)
        self.current_amount_entry.delete(0, tk.END)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item = self.tree.item(selected_item)
        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, item['values'][1])
        self.target_amount_entry.delete(0, tk.END)
        self.target_amount_entry.insert(0, item['values'][2])
        self.current_amount_entry.delete(0, tk.END)
        self.current_amount_entry.insert(0, item['values'][3])

    def load_goals(self):
        # Effacer les anciennes entrées
        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = create_connection("budget.db")
        if conn is not None:
            try:
                c = conn.cursor()
                c.execute("SELECT id, description, target_amount, current_amount FROM goals")
                rows = c.fetchall()
                for row in rows:
                    self.tree.insert("", "end", values=row)
            except sqlite3.Error as e:
                print(e)
            finally:
                conn.close()
        else:
            print("Error! Cannot create the database connection.")
