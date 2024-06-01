import tkinter as tk
from tkinter import messagebox
import sqlite3
from views.dashboard import Dashboard
from views.transactions import Transactions
from views.history import History
from views.budget_summary import BudgetSummary
from views.goals import Goals
from views.notes import Notes
from utils.db import create_tables
from PIL import Image, ImageTk, ImageFilter

# Fonction pour créer la base de données et la table des utilisateurs
def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Fenêtre de login
def show_login(on_success, on_register):
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Nom d'utilisateur").pack(pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Mot de passe").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()
        if check_credentials(username, password):
            login_window.destroy()
            on_success()
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    tk.Button(login_window, text="Se connecter", command=attempt_login).pack(pady=5)
    tk.Button(login_window, text="S'inscrire", command=lambda: [login_window.destroy(), on_register()]).pack(pady=5)

    login_window.mainloop()

# Fenêtre d'inscription
def show_register():
    register_window = tk.Tk()
    register_window.title("Inscription")
    register_window.geometry("300x200")

    tk.Label(register_window, text="Nom d'utilisateur").pack(pady=5)
    username_entry = tk.Entry(register_window)
    username_entry.pack(pady=5)

    tk.Label(register_window, text="Mot de passe").pack(pady=5)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack(pady=5)

    def attempt_register():
        username = username_entry.get()
        password = password_entry.get()
        if register_user(username, password):
            messagebox.showinfo("Succès", "Inscription réussie. Vous pouvez maintenant vous connecter.")
            register_window.destroy()
            show_login(lambda: App().mainloop(), show_register)
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur déjà pris")

    tk.Button(register_window, text="S'inscrire", command=attempt_register).pack(pady=5)
    register_window.mainloop()

# Vérifie les informations de connexion
def check_credentials(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Enregistre un nouvel utilisateur
def register_user(username, password):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

# Classe principale de l'application
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Budget")
        self.geometry("800x600")

        # Create a Canvas to hold the background image
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Load and blur the background image
        self.bg_image = Image.open("budget_app/gestion_budget.png")  # Replace with the path to your image
        self.bg_image = self.bg_image.filter(ImageFilter.GaussianBlur(5))
        self.bg_image = self.bg_image.resize((2000, 1200), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Add the background image to the Canvas
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create a Frame to hold other widgets on top of the Canvas
        self.container = tk.Frame(self.canvas, bg="white", bd=2, relief="groove")  # Add bg and border for better visibility
        self.container.place(relx=0.5, rely=0.5, anchor="center", width=600, height=400)  # Center the container

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

if __name__ == "__main__":
    create_db()
    create_tables()
    show_login(lambda: App().mainloop(), show_register)
