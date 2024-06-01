import tkinter as tk
from tkinter import messagebox
import sqlite3

class RegisterWindow:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        self.create_widgets()

    def create_widgets(self):
        self.root.title("Application de Gestion de Budget - Inscription")
        self.root.geometry("300x250")
        
        tk.Label(self.root, text="Nom d'utilisateur").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        
        tk.Label(self.root, text="Mot de passe").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        
        tk.Label(self.root, text="Confirmer le mot de passe").pack(pady=5)
        self.confirm_password_entry = tk.Entry(self.root, show="*")
        self.confirm_password_entry.pack(pady=5)
        
        tk.Button(self.root, text="S'inscrire", command=self.register_user).pack(pady=20)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if password != confirm_password:
            messagebox.showerror("Erreur d'inscription", "Les mots de passe ne correspondent pas.")
        else:
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                conn.close()
                messagebox.showinfo("Inscription réussie", "Vous êtes inscrit avec succès.")
                self.on_success()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erreur d'inscription", "Le nom d'utilisateur existe déjà.")

def show_register(on_success):
    root = tk.Tk()
    app = RegisterWindow(root, on_success)
    root.mainloop()
