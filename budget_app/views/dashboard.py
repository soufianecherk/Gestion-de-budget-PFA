import tkinter as tk

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Tableau de Bord", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=20)

        self.transactions_button = tk.Button(self, text="Transactions", 
                                             command=lambda: self.controller.show_frame("Transactions"), 
                                             font=("Helvetica", 12), height=2, width=20)
        self.transactions_button.pack(pady=10)

        self.history_button = tk.Button(self, text="Historique", 
                                        command=lambda: self.controller.show_frame("History"), 
                                        font=("Helvetica", 12), height=2, width=20)
        self.history_button.pack(pady=10)

        self.budget_summary_button = tk.Button(self, text="Résumé Budget", 
                                               command=lambda: self.controller.show_frame("BudgetSummary"), 
                                               font=("Helvetica", 12), height=2, width=20)
        self.budget_summary_button.pack(pady=10)

        self.goals_button = tk.Button(self, text="Objectifs", 
                                      command=lambda: self.controller.show_frame("Goals"), 
                                      font=("Helvetica", 12), height=2, width=20)
        self.goals_button.pack(pady=10)

        self.notes_button = tk.Button(self, text="Notes", 
                                      command=lambda: self.controller.show_frame("Notes"), 
                                      font=("Helvetica", 12), height=2, width=20)
        self.notes_button.pack(pady=10)

        self.logout_button = tk.Button(self, text="Déconnexion", 
                                       command=self.logout, 
                                       font=("Helvetica", 12))
        self.logout_button.pack(pady=20, side=tk.BOTTOM)

        # Centrage des éléments dans la fenêtre principale
        self.label.pack(anchor="center")

    def logout(self):
        self.controller.show_frame("Login")
