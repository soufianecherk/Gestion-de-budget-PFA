import tkinter as tk
from tkinter import messagebox
import sqlite3

class LoginWindow:
    def __init__(self, root, on_success, on_register):
        self.root = root
        self.on_success = on_success
        self.on_register = on_register
        self.create_widgets()

    def create_widgets(self):
        self.root.title("Application de Gestion de Budget - Login")
        self.root.geometry("300x250")
        
        tk.Label(self.root, text="Nom d'utilisateur").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        
        tk.Label(self.root, text="Mot de passe").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        
        tk.Button(self.root, text="Connexion", command=self.verify_login).pack(pady=10)
        tk.Button(self.root, text="S'inscrire", command=self.on_register).pack(pady=10)

    def verify_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Vérifier d'abord dans users.db
        if self.check_credentials(username, password, 'users.db'):
            messagebox.showinfo("Login réussi", "Bienvenue, vous êtes connecté.")
            self.on_success()
        # Vérifier ensuite dans admin.db si aucune correspondance dans users.db
        elif self.check_credentials(username, password, 'admin.db'):
            messagebox.showinfo("Login réussi", "Bienvenue, vous êtes connecté en tant qu'administrateur.")
            self.on_success()
        else:
            messagebox.showerror("Erreur de login", "Nom d'utilisateur ou mot de passe incorrect.")

    def check_credentials(self, username, password, database):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM admin WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None

def show_login(on_success, on_register):
    root = tk.Tk()
    app = LoginWindow(root, on_success, on_register)
    root.mainloop()

if __name__ == "__main__":
    show_login(lambda: print("Logged in"), lambda: print("Register clicked"))