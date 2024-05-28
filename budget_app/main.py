import tkinter as tk
from views.dashboard import Dashboard
from views.transactions import Transactions
from views.history import History
from views.budget_summary import BudgetSummary
from views.goals import Goals
from views.notes import Notes
from utils.db import create_tables
from PIL import Image, ImageTk, ImageFilter

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
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
    create_tables()  # Assurez-vous que les tables sont créées avant de lancer l'application
    app = App()
    app.mainloop()
