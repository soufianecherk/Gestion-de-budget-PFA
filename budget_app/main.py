import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk, ImageFilter
from views.dashboard import Dashboard
from views.transactions import Transactions
from views.history import History
from views.budget_summary import BudgetSummary
from views.goals import Goals
from views.notes import Notes
from views.graphs_window import GraphsWindow
from utils.db import create_tables

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
    login_window.geometry("700x400")
    login_window.configure(bg="#FFFFFF")  # Couleur de fond blanc
    
    # Charger l'image d'arrière-plan
    background_image = Image.open("budget_app/gestion_budget.png")
    background_image = background_image.resize((700, 400), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)

    # Créer un label pour afficher l'image d'arrière-plan
    background_label = tk.Label(login_window, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # Frame pour contenir les widgets de connexion afin de les placer au-dessus de l'image
    login_frame = tk.Frame(login_window, bg="#FFFFFF", bd=5)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    # Label de bienvenue
    welcome_label = tk.Label(login_window, text="Bienvenue, veuillez vous connecter", font=("Helvetica", 16, "bold"), fg="#333333")
    welcome_label.pack(pady=30)

    tk.Label(login_window, text="Nom d'utilisateur", font=("Helvetica", 14), fg="#333333").pack(pady=5)
    username_entry = tk.Entry(login_window, font=("Helvetica", 13))
    username_entry.pack(pady=5, ipadx=10)

    tk.Label(login_window, text="Mot de passe", font=("Helvetica", 14), fg="#333333").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*", font=("Helvetica", 13))
    password_entry.pack(pady=5, ipadx=10)

    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()
        if check_credentials(username, password):
            login_window.destroy()
            app = App(username)
            app.show_frame("Dashboard")
            app.mainloop()
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    tk.Button(login_window, text="Se connecter", font=("Helvetica", 13, "bold"), command=attempt_login, width=25, bg="#4CAF50", fg="white").pack(pady=(30,15))
    tk.Button(login_window, text="S'inscrire", font=("Helvetica", 13, "bold"), command=lambda: [login_window.destroy(), on_register()], width=25, bg="#2196F3", fg="white").pack(pady=3)

    login_window.mainloop()

# Fenêtre d'inscription
def show_register():
    def go_to_login():
        register_window.destroy()
        show_login(lambda username: App(username).mainloop(), show_register)

    register_window = tk.Tk()
    register_window.title("Inscription")
    register_window.geometry("700x450")
    register_window.configure(bg="#FFFFFF")  # Couleur de fond blanc

    # Charger l'image d'arrière-plan
    background_image = Image.open("budget_app/gestion_budget.png")
    background_image = background_image.filter(ImageFilter.GaussianBlur(2))
    background_image = background_image.resize((700, 450), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)

    # Créer un label pour afficher l'image d'arrière-plan
    background_label = tk.Label(register_window, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # Frame pour contenir les widgets de connexion afin de les placer au-dessus de l'image
    login_frame = tk.Frame(register_window, bg="#FFFFFF", bd=5)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Label de bienvenue
    welcome_label = tk.Label(register_window, text="Bienvenue, veuillez s'inscrire", font=("Helvetica", 16, "bold"), fg="#333333")
    welcome_label.pack(pady=30)

    tk.Label(register_window, text="Nom d'utilisateur", font=("Helvetica", 14), fg="#333333").pack(pady=5)
    username_entry = tk.Entry(register_window, font=("Helvetica", 13))
    username_entry.pack(pady=5, ipadx=10)

    tk.Label(register_window, text="Mot de passe", font=("Helvetica", 14), fg="#333333").pack(pady=5)
    password_entry = tk.Entry(register_window, show="*", font=("Helvetica", 13))
    password_entry.pack(pady=5, ipadx=10)

    def attempt_register():
        username = username_entry.get()
        password = password_entry.get()
        if register_user(username, password):
            messagebox.showinfo("Succès", "Inscription réussie. Vous pouvez maintenant vous connecter.")
            register_window.destroy()
            show_login(lambda username: App(username).mainloop(), show_register)
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur déjà pris")

    tk.Button(register_window, text="S'inscrire", font=("Helvetica", 13, "bold"), command=attempt_register, width=20, bg="#2196F3", fg="white").pack(pady=(20, 50))
    tk.Label(register_window, text="Vous avez déjà un compte? Connectez-vous ici.", font=("Helvetica", 12, "bold"), bg="#FFFFFF", fg="#4CAF50").pack(pady=5)
    tk.Button(register_window, text="Se connecter", font=("Helvetica", 12, "bold"), command=go_to_login, width=20, bg="#4CAF50", fg="white").pack(pady=(5, 20))

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
    def __init__(self, username):
        super().__init__()
        self.title("Gestion de Budget")
        self.geometry("1000x600")
        self.configure(bg="#FFFFFF")  # Couleur de fond blanc

        # Create a Canvas to hold the background image
        self.canvas = tk.Canvas(self, width=800, height=600, bg="#FFFFFF")
        self.canvas.pack(fill="both", expand=True)

        # Load and blur the background image
        self.bg_image = Image.open("budget_app/gestion_budget.png")  # Replace with the path to your image
        self.bg_image = self.bg_image.filter(ImageFilter.GaussianBlur(5))
        self.bg_image = self.bg_image.resize((2000, 1200), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Add the background image to the Canvas
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create a Frame to hold other widgets on top of the Canvas
        self.container = tk.Frame(self.canvas, bg="#FFFFFF", bd=2, relief="groove")
        self.container.place(relx=0.5, rely=0.5, anchor="center", width=900, height=500)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Transactions, History, BudgetSummary, Goals, Notes, Dashboard, GraphsWindow):  # Ajout de GraphsWindow ici
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")
    
    def show_frame(self, page_name):
        frame = self.frames.get(page_name)
        if frame:
            frame.tkraise()
        else:
            print(f"Frame '{page_name}' not found!")


if __name__ == "__main__":
    create_db()
    create_tables()
    show_login(lambda username: App(username).mainloop(), show_register)



            

