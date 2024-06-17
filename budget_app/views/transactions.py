import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from models.transaction import Transaction

class Transactions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Transactions", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10, padx=10)

        # Frame to hold the entry fields
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Date:").grid(row=0, column=0, padx=5, pady=3)
        self.date_entry = tk.Entry(entry_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(entry_frame, text="Category:").grid(row=1, column=0, padx=5, pady=3)
        self.category_entry = tk.Entry(entry_frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=3)

        tk.Label(entry_frame, text="Subcategory:").grid(row=2, column=0, padx=5, pady=3)
        self.subcategory_entry = tk.Entry(entry_frame)
        self.subcategory_entry.grid(row=2, column=1, padx=5, pady=3)

        tk.Label(entry_frame, text="Amount:").grid(row=3, column=0, padx=5, pady=3)
        self.amount_entry = tk.Entry(entry_frame)
        self.amount_entry.grid(row=3, column=1, padx=5, pady=3)

        tk.Label(entry_frame, text="Note:").grid(row=4, column=0, padx=5, pady=3)
        self.note_entry = tk.Entry(entry_frame)
        self.note_entry.grid(row=4, column=1, padx=5, pady=3)

        # Button frame to hold the action buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Add Transaction", command=self.add_transaction)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(button_frame, text="Edit Transaction", command=self.edit_transaction)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Delete Transaction", command=self.delete_transaction)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.clear_button = tk.Button(button_frame, text="Clear Fields", command=self.clear_entries)
        self.clear_button.grid(row=0, column=3, padx=5)

        self.back_button = tk.Button(self, text="Retour au Tableau de Bord", command=lambda: self.controller.show_frame("Dashboard"))
        self.back_button.pack(pady=10)

        # Treeview to display transactions
        self.transaction_tree = ttk.Treeview(self, columns=("ID", "Date", "Category", "Subcategory", "Amount", "Note"), show="headings")
        self.transaction_tree.heading("ID", text="ID")
        self.transaction_tree.heading("Date", text="Date")
        self.transaction_tree.heading("Category", text="Category")
        self.transaction_tree.heading("Subcategory", text="Subcategory")
        self.transaction_tree.heading("Amount", text="Amount")
        self.transaction_tree.heading("Note", text="Note")
        self.transaction_tree.pack(padx=10, pady=10)

        self.transaction_tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Load transactions initially
        self.load_transactions()

    def load_transactions(self):
        # Clear existing items in the treeview
        for i in self.transaction_tree.get_children():
            self.transaction_tree.delete(i)
        
        # Fetch all transactions from the database
        transactions = self.get_all_transactions()
        
        # Insert each transaction into the treeview
        for transaction in transactions:
            self.transaction_tree.insert("", tk.END, values=(transaction.id, transaction.date, transaction.category, transaction.subcategory, transaction.amount, transaction.note))

    def get_all_transactions(self):
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM transactions')
        rows = cursor.fetchall()
        conn.close()
        
        transactions = []
        for row in rows:
            transaction = Transaction(*row)
            transactions.append(transaction)
        
        return transactions

    def add_transaction(self):
        # Fetch data from entry fields
        date = self.date_entry.get()
        category = self.category_entry.get()
        subcategory = self.subcategory_entry.get()
        amount = float(self.amount_entry.get())
        note = self.note_entry.get()

        # Create a new Transaction object and save it to the database
        transaction = Transaction(None, date, category, subcategory, amount, note)
        transaction.save()

        # Reload transactions in the treeview and clear entry fields
        self.load_transactions()
        self.clear_entries()

    def edit_transaction(self):
        selected_item = self.transaction_tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Aucune transaction sélectionnée.")
            return

        # Fetch data from entry fields
        transaction_id = self.transaction_tree.item(selected_item, "values")[0]
        date = self.date_entry.get()
        category = self.category_entry.get()
        subcategory = self.subcategory_entry.get()
        amount = float(self.amount_entry.get())
        note = self.note_entry.get()

        # Update the selected transaction
        transaction = Transaction(transaction_id, date, category, subcategory, amount, note)
        transaction.update()

        # Reload transactions in the treeview and clear entry fields
        self.load_transactions()
        self.clear_entries()

    def delete_transaction(self):
        selected_item = self.transaction_tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Aucune transaction sélectionnée.")
            return

        # Fetch transaction ID from the selected item
        transaction_id = self.transaction_tree.item(selected_item, "values")[0]

        # Delete the selected transaction
        transaction = Transaction(transaction_id, None, None, None, None, None)
        transaction.delete()

        # Reload transactions in the treeview and clear entry fields
        self.load_transactions()
        self.clear_entries()

    def clear_entries(self):
        # Clear all entry fields
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.subcategory_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.note_entry.delete(0, tk.END)

    def on_tree_select(self, event):
        # Populate entry fields when a transaction is selected in the treeview
        selected_item = self.transaction_tree.selection()
        if selected_item:
            transaction_id, date, category, subcategory, amount, note = self.transaction_tree.item(selected_item, "values")
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, date)
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, category)
            self.subcategory_entry.delete(0, tk.END)
            self.subcategory_entry.insert(0, subcategory)
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, amount)
            self.note_entry.delete(0, tk.END)
            self.note_entry.insert(0, note)

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("800x600")
    app.title("Gestion de Budget")

    # Replace with the correct database path
    conn = sqlite3.connect('budget.db')
    conn.close()

    app.mainloop()
