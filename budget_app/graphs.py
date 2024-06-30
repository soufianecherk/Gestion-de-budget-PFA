# graphs.py

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import tkinter as tk

class GraphsWindow:
    def __init__(self, master, data):
        self.master = master
        self.master.title("Graphs")
        self.data = data
        self.create_widgets()

    def create_widgets(self):
        # Create a button to show the matplotlib graph
        self.matplotlib_button = tk.Button(self.master, text="Show Matplotlib Graph", command=self.show_matplotlib_graph)
        self.matplotlib_button.pack(pady=10)

        # Create a button to show the seaborn graph
        self.seaborn_button = tk.Button(self.master, text="Show Seaborn Graph", command=self.show_seaborn_graph)
        self.seaborn_button.pack(pady=10)

        # Create a button to show the plotly graph
        self.plotly_button = tk.Button(self.master, text="Show Plotly Graph", command=self.show_plotly_graph)
        self.plotly_button.pack(pady=10)

    def show_matplotlib_graph(self):
        # Sample data from the database
        data = self.data

        # Create a histogram using matplotlib
        plt.figure(figsize=(10, 6))
        plt.hist(data['column_name'], bins=30, alpha=0.75, color='blue', edgecolor='black')
        plt.title('Matplotlib Histogram')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

    def show_seaborn_graph(self):
        # Sample data from the database
        data = self.data

        # Create a histogram using seaborn
        plt.figure(figsize=(10, 6))
        sns.histplot(data['column_name'], bins=30, kde=True, color='blue')
        plt.title('Seaborn Histogram')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

    def show_plotly_graph(self):
        # Sample data from the database
        data = self.data

        # Create a bar chart using plotly
        fig = px.bar(data, x='Category', y='Values', title='Plotly Bar Chart')
        fig.show()

# Exemple d'utilisation de la classe GraphsWindow
if __name__ == "__main__":
    import pandas as pd
    import numpy as np

    root = tk.Tk()
    sample_data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': np.random.randint(10, 100, 4),
        'column_name': np.random.randn(1000)
    })
    app = GraphsWindow(root, sample_data)
    root.mainloop()


