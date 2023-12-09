import csv
import tkinter as tk
from tkinter import filedialog

def extract_emails(csv_file):
    emails = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row['E-mail']
            emails.append(email)
    return emails

def set_file_path():
    file_path = filedialog.askopenfilename(title="Browse", filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(tk.END, file_path)

def generate_emails():
    file_path = file_path_entry.get()
    if file_path:
        emails = extract_emails(file_path)
        for email in emails:
            email_listbox.insert(tk.END, email)

# Ablak létrehozása
window = tk.Tk()
window.title("Email Extractor")

# Távolság az ablak fejlécétől
header_padding = tk.Label(window, text="", height=2)
header_padding.pack()

# Szöveg a "Browse" gomb fölött
browse_label = tk.Label(window, text="Browse to the CSV file:", font=("Helvetica", 12))
browse_label.pack(anchor='w', padx=10)

# Elérési út mező és Tallózás gomb egy sorban, bal szélre
file_path_frame = tk.Frame(window)
file_path_frame.pack(pady=10, padx=10, anchor='w')

file_path_entry = tk.Entry(file_path_frame, width=40)
file_path_entry.pack(side=tk.LEFT)

browse_button = tk.Button(file_path_frame, text="Browse", command=set_file_path)
browse_button.pack(side=tk.LEFT, padx=5)

# Lista a kigyűjtött emailek megjelenítéséhez
email_listbox = tk.Listbox(window, selectmode=tk.SINGLE, width=50, height=10)
email_listbox.pack(side=tk.LEFT, padx=10, pady=10)

# CSV importálás gomb jobb alsó sarokban
import_button = tk.Button(window, text="Generate", command=generate_emails)
import_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Ablak méret beállítása
window.geometry("600x300")

# Ablak indítása
window.mainloop()
