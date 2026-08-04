import tkinter as tk
from tkinter import filedialog

# Tkinter GUI 
root = tk.Tk()
root.withdraw() 

# selectfile
file_path = filedialog.askopenfilename(title="select a .txt file", filetypes=[("Text Files", "*.txt")])

if file_path:
    # read file
    with open(file_path, 'r') as file:
        data = file.readlines()

    # remove
    data = [line.strip() for line in data]

    # Remove duplicate lines
    unique_data = list(set(data))

    # write
    with open(file_path, 'w') as file:
        for item in unique_data:
            file.write(f"{item}\n")

    print(f"Duplicate lines were successfully removed and '{file_path}' saved to file.")
else:
    print("No file selected.")
