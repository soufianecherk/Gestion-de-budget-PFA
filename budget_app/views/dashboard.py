import tkinter as tk
from tkinter import messagebox

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Couleurs et styles
        bg_color = "#F0F0F0"  # Fond gris clair
        btn_color = "#4CAF50"  # Vert pour les boutons
        btn_font = ("Helvetica", 12, "bold")
        lbl_font = ("Helvetica", 16, "bold")

        self.configure(bg=bg_color)

        self.label = tk.Label(self, text="Tableau de Bord", font=lbl_font, bg=bg_color, fg="#333333")
        self.label.pack(pady=20)

        button_style = {"font": btn_font, "bg": btn_color, "fg": "white", "height": 2, "width": 25}

        self.transactions_button = tk.Button(self, text="Transactions", 
                                             command=lambda: self.controller.show_frame("Transactions"), 
                                             **button_style)
        self.transactions_button.pack(pady=10)

        self.history_button = tk.Button(self, text="Historique", 
                                        command=lambda: self.controller.show_frame("History"), 
                                        **button_style)
        self.history_button.pack(pady=10)

        self.budget_summary_button = tk.Button(self, text="Résumé Budget", 
                                               command=lambda: self.controller.show_frame("BudgetSummary"), 
                                               **button_style)
        self.budget_summary_button.pack(pady=10)

        self.goals_button = tk.Button(self, text="Objectifs", 
                                      command=lambda: self.controller.show_frame("Goals"), 
                                      **button_style)
        self.goals_button.pack(pady=10)

        self.notes_button = tk.Button(self, text="Notes", 
                                      command=lambda: self.controller.show_frame("Notes"), 
                                      **button_style)
        self.notes_button.pack(pady=10)

        self.graphs_button = tk.Button(self, text="Graphiques", 
                                       command=lambda: self.controller.show_frame("GraphsWindow"), 
                                       **button_style)
        self.graphs_button.pack(pady=10)

        self.logout_button = tk.Button(self, text="Déconnexion", 
                                       command=self.controller.logout, 
                                       font=btn_font, bg="#E53935", fg="white")
        self.logout_button.pack(pady=20, side=tk.BOTTOM)