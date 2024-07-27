import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

def plot_scatter_matrix():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        scatter_matrix(df, alpha=0.5, figsize=(10, 10))
        plt.show()

# Create the main application window
root = tk.Tk()
root.title("Scatter Matrix Plot")

# Create a button to open the CSV file
open_button = tk.Button(root, text="Open CSV File", command=plot_scatter_matrix)
open_button.pack()

# Run the Tkinter main loop
root.mainloop()
