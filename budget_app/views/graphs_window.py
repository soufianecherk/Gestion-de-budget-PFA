import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sqlite3
import pandas as pd

class GraphsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Graphiques", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=20)

        self.plot_button = tk.Button(self, text="Générer Graphique", command=self.generate_plot, font=("Helvetica", 12), height=2, width=20)
        self.plot_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Retour au Tableau de Bord", command=lambda: controller.show_frame("Dashboard"), font=("Helvetica", 12), height=2, width=20)
        self.back_button.pack(pady=10)

        self.canvas = None

    def generate_plot(self):
        conn = sqlite3.connect('budget.db')
        df = pd.read_sql_query("SELECT * FROM transactions", conn)
        conn.close()

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        df.groupby('category')['amount'].sum().plot(kind='bar', ax=ax)

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=10)
