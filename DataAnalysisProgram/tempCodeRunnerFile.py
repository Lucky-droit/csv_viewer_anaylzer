def open_file():
    global data , data_copy
    filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filename:
        data = load_csv(filename)
        if data:
            columns = data[0] 
            data_copy = data # Extract column names from the header row
            data = data[1:]  # Remove the header row
            display_table(data, columns)
