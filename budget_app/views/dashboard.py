import tkinter as tk
from tkinter import ttk

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Dashboard")
        self.label.pack(pady=10, padx=10)
