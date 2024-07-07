import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class AdminApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Gestion des Utilisateurs", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10, padx=10)

        # Frame to hold the entry fields
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Nom d'utilisateur:").grid(row=0, column=0, padx=5, pady=3)
        self.username_entry = tk.Entry(entry_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(entry_frame, text="Mot de passe:").grid(row=1, column=0, padx=5, pady=3)
        self.password_entry = tk.Entry(entry_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=3)

        # Button frame to hold the action buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Ajouter Utilisateur", command=self.add_user)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(button_frame, text="Modifier Utilisateur", command=self.edit_user)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Supprimer Utilisateur", command=self.delete_user)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.clear_button = tk.Button(button_frame, text="Effacer Champs", command=self.clear_entries)
        self.clear_button.grid(row=0, column=3, padx=5)

        self.back_button = tk.Button(self, text="Retour au Tableau de Bord", command=lambda: self.controller.show_frame("Dashboard"))
        self.back_button.pack(pady=10)

        # Treeview to display users
        self.user_tree = ttk.Treeview(self, columns=("ID", "Username", "Password"), show="headings")
        self.user_tree.heading("ID", text="ID")
        self.user_tree.heading("Username", text="Nom d'utilisateur")
        self.user_tree.heading("Password", text="Mot de passe")
        self.user_tree.pack(padx=10, pady=10)

        self.user_tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Load users initially
        self.load_users()

    def load_users(self):
        # Clear existing items in the treeview
        for i in self.user_tree.get_children():
            self.user_tree.delete(i)
        
        # Fetch all users from the database
        users = self.get_all_users()
        
        # Insert each user into the treeview
        for user in users:
            self.user_tree.insert("", tk.END, values=(user['id'], user['username'], user['password']))

    def get_all_users(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, password FROM users')
        rows = cursor.fetchall()
        conn.close()
        
        users = []
        for row in rows:
            user = {'id': row[0], 'username': row[1], 'password': row[2]}
            users.append(user)
        
        return users

    def add_user(self):
        # Fetch data from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Insert the new user into the database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()

        # Reload users in the treeview and clear entry fields
        self.load_users()
        self.clear_entries()

    def edit_user(self):
        selected_item = self.user_tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Aucun utilisateur sélectionné.")
            return

        # Fetch data from entry fields
        user_id = self.user_tree.item(selected_item, "values")[0]
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Update the selected user
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET username=?, password=? WHERE id=?', (username, password, user_id))
        conn.commit()
        conn.close()

        # Reload users in the treeview and clear entry fields
        self.load_users()
        self.clear_entries()

    def delete_user(self):
        selected_item = self.user_tree.selection()
        if not selected_item:
            messagebox.showwarning("Avertissement", "Aucun utilisateur sélectionné.")
            return

        # Fetch user ID from the selected item
        user_id = self.user_tree.item(selected_item, "values")[0]

        # Delete the selected user
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
        conn.commit()
        conn.close()

        # Reload users in the treeview and clear entry fields
        self.load_users()
        self.clear_entries()

    def clear_entries(self):
        # Clear all entry fields
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def on_tree_select(self, event):
        # Populate entry fields when a user is selected in the treeview
        selected_item = self.user_tree.selection()
        if selected_item:
            user_id, username, password = self.user_tree.item(selected_item, "values")
            self.username_entry.delete(0, tk.END)
            self.username_entry.insert(0, username)
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)

# Utilisation
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Gestion des Utilisateurs")
    app = AdminApp(root, None)
    app.pack(fill="both", expand=True)
    root.mainloop()