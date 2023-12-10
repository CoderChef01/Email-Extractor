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

def save_emails():
    emails_to_save = email_listbox.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for email in emails_to_save:
                writer.writerow([email])

def load_emails():
    file_path = filedialog.askopenfilename(title="Load CSV", filetypes=[("CSV files", "*.csv")])
    if file_path:
        email_listbox.delete(0, tk.END)
        emails = extract_emails(file_path)
        for email in emails:
            email_listbox.insert(tk.END, email)

def open_settings():
    # Ide jöhetnek a beállítások kezeléséhez szükséges kódok
    pass

def open_help():
    # Ide jöhetnek a súgókezeléshez szükséges kódok
    pass

def open_about():
    about_window = tk.Toplevel(window)
    about_window.title("About")

    about_label = tk.Label(about_window, text="Email Extractor v1.2\n\n2023\n\nCreated by CoderChef", font=("Arial", 12))
    about_label.pack(padx=20, pady=20)

# Ablak létrehozása
window = tk.Tk()
window.title("Email Extractor")

# Menü létrehozása
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# "File" menü
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save", command=save_emails)
file_menu.add_command(label="Load", command=load_emails)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)

# "Settings" menü
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)

settings_menu.add_command(label="Options", command=open_settings)

# "Help" menü
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="About", command=open_about)

# Távolság az ablak fejlécétől
header_padding = tk.Label(window, text="", height=2)
header_padding.pack()

# Szöveg a "Browse" gomb fölött
browse_label = tk.Label(window, text="Browse to the CSV file:", font=("Arial", 12), background="lightgrey")
browse_label.pack(anchor='w', padx=10)

# Elérési út mező és Tallózás gomb egy sorban, bal szélre
file_path_frame = tk.Frame(window)
file_path_frame.pack(pady=10, padx=10, anchor='w')

file_path_entry = tk.Entry(file_path_frame, width=40, font=("Arial", 10))
file_path_entry.pack(side=tk.LEFT)

browse_button = tk.Button(file_path_frame, text="Browse", command=set_file_path, font=("Arial", 10))
browse_button.pack(side=tk.LEFT, padx=5)

# Lista a kigyűjtött emailek megjelenítéséhez
email_listbox = tk.Listbox(window, selectmode=tk.SINGLE, width=50, height=10, font=("Arial", 10), bg="lightgrey")
email_listbox.pack(side=tk.LEFT, padx=10, pady=10)

# CSV importálás gomb jobb alsó sarokban
import_button = tk.Button(window, text="Generate", command=generate_emails, font=("Arial", 12))
import_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Ablak méret beállítása
window.geometry("480x300")

# Ablak indítása
window.mainloop()
