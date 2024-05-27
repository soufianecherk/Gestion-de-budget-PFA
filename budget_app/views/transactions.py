import tkinter as tk
from tkinter import ttk
from models.transaction import Transaction

class Transactions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Transactions")
        self.label.pack(pady=10, padx=10)

        self.date_entry = tk.Entry(self)
        self.date_entry.pack()

        self.category_entry = tk.Entry(self)
        self.category_entry.pack()

        self.subcategory_entry = tk.Entry(self)
        self.subcategory_entry.pack()

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        self.note_entry = tk.Entry(self)
        self.note_entry.pack()

        self.add_button = tk.Button(self, text="Add Transaction", command=self.add_transaction)
        self.add_button.pack()

    def add_transaction(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        subcategory = self.subcategory_entry.get()
        amount = float(self.amount_entry.get())
        note = self.note_entry.get()

        transaction = Transaction(date, category, subcategory, amount, note)
        transaction.save()
