import tkinter as tk

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Tableau de Bord")
        self.label.pack(pady=10, padx=10)

        self.transactions_button = tk.Button(self, text="Transactions", 
                                             command=lambda: self.controller.show_frame("Transactions"))
        self.transactions_button.pack(pady=5)

        self.history_button = tk.Button(self, text="Historique", 
                                        command=lambda: self.controller.show_frame("History"))
        self.history_button.pack(pady=5)

        self.budget_summary_button = tk.Button(self, text="Résumé Budget", 
                                               command=lambda: self.controller.show_frame("BudgetSummary"))
        self.budget_summary_button.pack(pady=5)

        self.goals_button = tk.Button(self, text="Objectifs", 
                                      command=lambda: self.controller.show_frame("Goals"))
        self.goals_button.pack(pady=5)

        self.notes_button = tk.Button(self, text="Notes", 
                                      command=lambda: self.controller.show_frame("Notes"))
        self.notes_button.pack(pady=5)
