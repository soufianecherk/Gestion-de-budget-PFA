import tkinter as tk

class Notes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Notes")
        self.label.pack(pady=10, padx=10)

        self.text = tk.Text(self, wrap="word")
        self.text.pack(fill="both", expand=True)

        self.save_button = tk.Button(self, text="Enregistrer Note", command=self.save_note)
        self.save_button.pack()

    def save_note(self):
        note_content = self.text.get("1.0", tk.END)
        with open("notes.txt", "a") as file:
            file.write(note_content + "\n")
        self.text.delete("1.0", tk.END)

    # Ajout d'un bouton pour revenir au tableau de bord
        self.back_button = tk.Button(self, text="Retour au Tableau de Bord", 
                                     command=lambda: self.controller.show_frame("Dashboard"))
        self.back_button.pack(pady=5)