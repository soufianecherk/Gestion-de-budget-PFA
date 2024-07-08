import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sqlite3
import pandas as pd

class GraphsWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Couleurs et styles
        bg_color = "#F0F0F0"  # Fond gris clair
        btn_color = "#4CAF50"  # Vert pour les boutons
        btn_font = ("Helvetica", 12, "bold")
        lbl_font = ("Helvetica", 16, "bold")

        self.configure(bg=bg_color)

        self.label = tk.Label(self, text="Graphiques", font=lbl_font, bg=bg_color, fg="#333333")
        self.label.pack(pady=20)

        # Frame pour les boutons
        button_frame = tk.Frame(self, bg=bg_color)
        button_frame.pack(pady=10)

        self.plot_button = tk.Button(button_frame, text="Générer Graphique", command=self.generate_plot, font=btn_font, bg=btn_color, fg="white", height=2, width=25)
        self.plot_button.pack(side=tk.LEFT, padx=10)

        self.back_button = tk.Button(button_frame, text="Retour au Tableau de Bord", command=lambda: controller.show_frame("Dashboard"), font=btn_font, bg=btn_color, fg="white", height=2, width=25)
        self.back_button.pack(side=tk.LEFT, padx=10)

        self.canvas = None

    def generate_plot(self):
        conn = sqlite3.connect('budget.db')
        df = pd.read_sql_query("SELECT * FROM transactions", conn)
        conn.close()

        fig = Figure(figsize=(7, 6), dpi=100)
        ax = fig.add_subplot(111)

        df.groupby('category')['amount'].sum().plot(kind='bar', ax=ax, color="#4CAF50")

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=10)
