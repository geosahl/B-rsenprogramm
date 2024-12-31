import requests
import tkinter as tk

def fetch_german_companies():
    # Mock API response
    german_companies = ["Volkswagen", "Siemens", "Deutsche Bank", "Apple"]
    return german_companies

def open_german_companies_window():
    german_companies_window = tk.Toplevel(root)
    german_companies_window.title("German Companies")
    german_companies_list = fetch_german_companies()
    listbox = tk.Listbox(german_companies_window)
    for company in german_companies_list:
        listbox.insert(tk.END, company)
    listbox.pack()

root = tk.Tk()
root.title("Börsenprogramm")

german_companies_button = tk.Button(root, text="German Companies", command=open_german_companies_window)
german_companies_button.pack()

root.mainloop()
