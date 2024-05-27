import tkinter as tk
from views.dashboard import Dashboard
from views.transactions import Transactions
from views.history import History
from views.budget_summary import BudgetSummary
from views.goals import Goals
from views.notes import Notes
from utils.db import create_tables  # Ajoutez cette ligne

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Gestion de Budget")
        self.geometry("800x600")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Dashboard, Transactions, History, BudgetSummary, Goals, Notes):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Dashboard")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def create_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_command(label="Tableau de Bord", command=lambda: self.show_frame("Dashboard"))
        file_menu.add_command(label="Transactions", command=lambda: self.show_frame("Transactions"))
        file_menu.add_command(label="Historique", command=lambda: self.show_frame("History"))
        file_menu.add_command(label="Résumé Budget", command=lambda: self.show_frame("BudgetSummary"))
        file_menu.add_command(label="Objectifs", command=lambda: self.show_frame("Goals"))
        file_menu.add_command(label="Notes", command=lambda: self.show_frame("Notes"))
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit)

if __name__ == "__main__":
    create_tables()  # Ajoutez cette ligne pour créer les tables avant de lancer l'application
    app = App()
    app.create_menu()
    app.mainloop()
