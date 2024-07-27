import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import seaborn as sns
import csv
import subprocess
import pandas as pd
import matplotlib.pyplot as plt  

import matplotlib as plt 
from functools import partial 
from pandas.plotting import scatter_matrix
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
data = []
data_copy = []
description_displayed = False  # Keep track of whether the description is displayed
head_displayed = False
info_displayed = False
global df 

def load_csv(filename):
    global df 
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        df = pd.read_csv(filename)

    
    return data

def info():
    global data_copy, info_displayed , df
    if not head_displayed:
        if data_copy:
            # df = pd.DataFrame(data_copy, columns=data_copy[0]) 
            info_data = df.info()
            print(info_data)
            # info_text.config(text=info_data.to_string())
            info_displayed = True
    else:
        info_data.config(text="")
        info_displayed = False
def head():
    global data, head_displayed
    if not head_displayed:
        if data_copy:
            df = pd.DataFrame(data_copy, columns=data_copy[0]) 
            head_data = df.head()
            head_text.config(text=head_data.to_string())
            head_displayed = True
    else:
        head_text.config(text="")
        head_displayed = False
def display_info_in_window():  # Add a parameter for data_copy
    # Create a Tkinter window
    df = pd.DataFrame(data_copy, columns=data_copy[0])
def corr() : 
    global df 
    corr_data = df.corr() 
    print(corr_data)
def calculate_and_display_correlation():
    global df

    if df is not None:
        # Check if there are numerical columns in the DataFrame
        numerical_columns = df.select_dtypes(include=[float, int]).columns

        if not numerical_columns.empty:
            # If there are numerical columns, calculate the correlation matrix
            correlation_matrix = df[numerical_columns].corr()

            # Create a new window to display the correlation matrix
            window = tk.Toplevel()
            window.title("Correlation Matrix")

            # Create a Text widget to display the correlation matrix
            correlation_text = tk.Text(window, wrap=tk.WORD)
            correlation_text.pack()

            # Display the correlation matrix in the Text widget
            correlation_text.insert(tk.END, "Correlation Matrix:\n")
            correlation_text.insert(tk.END, correlation_matrix)

            window.mainloop()
        else:
            # If there are no numerical columns, display a message
            result_label.config(text="No numerical columns for correlation matrix")

# def open_file():
#     global data, data_copy
#     filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
#     if filename:
#         data = load_csv(filename)
#         if data:
#             columns = data[0]
#             data_copy = data
#             data = data[1:]
            
#             # Attempt to convert columns to numerical types
#             for col in columns:
#                 try:
#                     data_copy[0].index(col)
#                     data_copy[1:] = [[float(val) if val.replace('.', '', 1).isdigit() else val for val in row] for row in data_copy[1:]]
#                 except ValueError:
#                     pass
            
#             display_table(data, columns)
def display_table(data, columns):

    tree.delete(*tree.get_children())  # Clear existing data
    tree['columns'] = columns  # Set the columns dynamically
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Set a default width, adjust as needed
    
    for row in data:
        tree.insert('', 'end', values=row)
    df = pd.DataFrame(data_copy, columns=data_copy[0])
    shape_data = df.shape
    shape_text.config(text=shape_data)
def display_outliers():
    global data_copy

    if data_copy:
        df = pd.DataFrame(data_copy, columns=data_copy[0])

        # Check if there are numerical columns in the DataFrame
        numerical_columns = df.select_dtypes(include=[float, int]).columns

        if not numerical_columns.empty:
            # If there are numerical columns, calculate and display outliers
            fig, axes = plt.subplots(nrows=len(numerical_columns), figsize=(10, 5 * len(numerical_columns)))
            plt.subplots_adjust(hspace=0.5)
            
            for i, col in enumerate(numerical_columns):
                ax = axes[i]
                ax.boxplot(df[col], vert=False)
                ax.set_title(f"Boxplot of {col}")
                
            plt.show()
        else:
            # If there are no numerical columns, display a message
            result_label.config(text="No numerical columns for outlier detection")

def open_file():

    global data , data_copy
    filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filename:
        data = load_csv(filename)
        if data:
            columns = data[0] 
            data_copy = data # Extract column names from the header row
            data = data[1:]  # Remove the header row
            # set_column_data_types()
            display_table(data, columns)
    

def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")
    label = tk.Label(new_window, text="Hello, World!")
    label.pack()
def display_scatter_matrix():
    global data_copy

    if data_copy:
        df = pd.DataFrame(data_copy, columns=data_copy[0])

        # Explicitly specify the columns you want for the scatter matrix
        # columns_to_include = ["X", "Y", "Z"]  # Replace with your column names
        # numerical_columns = df[columns_to_include].select_dtypes(include=[float, int]).columns
        print(df.info())
        numerical_columns = df.select_dtypes(include=[float, int]).columns

        print(numerical_columns)
        if not numerical_columns.empty:
            # If there are numerical columns, create the scatter matrix
            scatter_matrix(df[columns_to_include], alpha=0.5, figsize=(10, 10))
            plt.suptitle("Scatter Matrix")

            # Embed the plot in the tkinter window
            fig = plt.gcf()
            canvas = FigureCanvasTkAgg(fig, master=app)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=10, column=0, columnspan=3)
            canvas_widget.draw()
        else:
            # If there are no numerical columns, display a message
            result_label.config(text="No numerical columns for scatter matrix")


def calculate_sum():
    global data
    column_number = int(column_entry.get())
    total = 0

    if 0 <= column_number < len(data[0]):
        for row in data:
            if row:
                try:
                    total += float(row[column_number])
                except ValueError:
                    pass

        result_label.config(text=f"Sum of Column {column_number + 1}: {total}")
    else:
        result_label.config(text="Invalid column number")

def show_description():
    global data_copy, description_displayed
    if not description_displayed:
        if data_copy:
            df = pd.DataFrame(data_copy, columns=data_copy[0])
            description = df.describe()
            description_text.config(text=description.to_string())
            description_displayed = True
    else:
        description_text.config(text="")
        description_displayed = False

def display_info_in_window() : 
        global data_copy
        df = pd.DataFrame(data_copy, columns=data_copy[0])
        print(df.info())
def display_outliers():
    global df

    if df is not None:
        # Check if there are numerical columns in the DataFrame
        numerical_columns = df.select_dtypes(include=[float, int]).columns

        if not numerical_columns.empty:
            # Create a new window to display the outliers
            window = tk.Toplevel()
            window.title("Outliers")

            y_position = 20
            for col in numerical_columns:
                outlier_data = get_outlier_data(df[col])
                outlier_text = tk.Text(window, wrap=tk.WORD)
                outlier_text.insert(tk.END, f"Outliers for {col}:\n\n")
                outlier_text.insert(tk.END, outlier_data)
                outlier_text.pack()
                y_position += 220

            window.mainloop()
        else:
            # If there are no numerical columns, display a message
            result_label.config(text="No numerical columns for outlier detection")

def get_outlier_data(column_data):
    # Define your outlier detection logic here
    # For example, you can use IQR method to find outliers
    Q1 = column_data.quantile(0.25)
    Q3 = column_data.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = column_data[(column_data < lower_bound) | (column_data > upper_bound)]

    return outliers
# ... (rest of your code)






# def crop_data():
#     global data
#     try:
#         column_number = int(crop_column_entry.get())
#         start_row = int(crop_start_row_entry.get())
#         end_row = int(crop_end_row_entry.get())
#         if (
#             0 <= column_number < len(data[0])
#             and 0 <= start_row < len(data)
#             and 0 <= end_row < len(data)
#             and start_row <= end_row
#         ):
#             cropped_data = [data[i][column_number] for i in range(start_row, end_row + 1)]
#             print(cropped_data)
#             display_table([cropped_data], [f'Cropped Column {column_number}'])
#         else:
#             display_table([], [])
#     except ValueError:
#         display_table([], [])
app = tk.Tk()
app.title("CSV Viewer")

frame = ttk.Frame(app)
frame.grid(row=0, column=0, sticky='nsew')

tree = ttk.Treeview(frame, show='headings')
tree.grid(row=0, column=0, sticky='nsew')

open_button = ttk.Button(app, text="Open CSV", command=open_file)
open_button.grid(row=0, column=1, sticky='n')

new_window_button = ttk.Button(app, text="Click Me", command=open_new_window)
new_window_button.grid(row=0, column=2, sticky='n')

new_window_button = ttk.Button(app, text="Head", command=head)
new_window_button.grid(row=0, column=3, sticky='n')

info_button = ttk.Button(app, text="Info", command=info)
info_button.grid(row=0, column=4, sticky='n')

outliers_button = ttk.Button(app, text="Display Outliers", command=display_outliers)
outliers_button.grid(row=10, column=0, columnspan=3)

outliers_button = ttk.Button(app, text="outliers", command=display_outliers)
outliers_button.grid(row=0, column=5, sticky='n')

# info_button = ttk.Button(app, text="Info", command=partial(display_info_in_window, data_copy))
# info_button.grid(row=0, column=4, sticky='n')



column_entry_label = ttk.Label(app, text="Enter Column Number:")
column_entry_label.grid(row=1, column=0, sticky='e')

column_entry = ttk.Entry(app)
column_entry.grid(row=1, column=1, sticky='w')

calculate_button = ttk.Button(app, text="Calculate Sum", command=calculate_sum)
calculate_button.grid(row=1, column=2, sticky='w')

result_label = ttk.Label(app, text="")
result_label.grid(row=2, column=0, columnspan=3)

description_button = ttk.Button(app, text="Show Description", command=show_description)
description_button.grid(row=3, column=0, columnspan=3, sticky='n')

correlation_button = ttk.Button(app, text="Calculate Correlation", command=calculate_and_display_correlation)
correlation_button.grid(row=9, column=0, columnspan=3)


description_text = ttk.Label(app, text="")
description_text.grid(row=4, column=0, columnspan=3)

head_text = ttk.Label(app, text="")
head_text.grid(row=5, column=0, columnspan=3)

info_text = ttk.Label(app, text="")
info_text.grid(row=6, column=0, columnspan=3)

shape_text = ttk.Label(app, text="")
shape_text.grid(row=7, column=0, columnspan=3)




# scatter_matrix_button = ttk.Button(app, text="Scatter Matrix", command=display_scatter_matrix)
# scatter_matrix_button.grid(row=9, column=0, columnspan=3)



#

# crop_column_label = ttk.Label(app, text="Column Number:")
# crop_column_label.grid(row=5, column=0, sticky='e')

# crop_column_entry = ttk.Entry(app)
# crop_column_entry.grid(row=5, column=1, sticky='w')

# crop_start_row_label = ttk.Label(app, text="Start Row:")
# crop_start_row_label.grid(row=6, column=0, sticky='e')

# crop_start_row_entry = ttk.Entry(app)
# crop_start_row_entry.grid(row=6, column=1, sticky='w')

# crop_end_row_label = ttk.Label(app, text="End Row:")
# crop_end_row_label.grid(row=7, column=0, sticky='e')

# crop_end_row_entry = ttk.Entry(app)
# crop_end_row_entry.grid(row=7, column=1, sticky='w')

# crop_button = ttk.Button(app, text="Crop Data", command=crop_data)
# crop_button.grid(row=8, column=0, columnspan=3)

app.mainloop()
