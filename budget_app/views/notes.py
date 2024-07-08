import tkinter as tk

class Notes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

   

    def create_widgets(self):
        self.label = tk.Label(self, text="Notes", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10, padx=10)

        self.text = tk.Text(self, wrap="word")
        self.text.pack(fill="both", expand=True)

        btn_color = "#4CAF50"  # Vert pour les boutons
        btn_font = ("Helvetica", 12, "bold")
        
        self.save_button = tk.Button(self, text="Enregistrer Note", command=self.save_note, font=btn_font, bg = btn_color, fg = "white")
        self.save_button.pack()

        # Ajout d'un bouton pour revenir au tableau de bord
        self.back_button = tk.Button(self, text="Retour au Tableau de Bord", 
                                     command=lambda: self.controller.show_frame("Dashboard"), font=btn_font, bg="#2196F3", fg="white")
        self.back_button.pack(pady=5)

    def save_note(self):
        note_content = self.text.get("1.0", tk.END)
        with open("notes.txt", "a") as file:
            file.write(note_content + "\n")
        self.text.delete("1.0", tk.END)

