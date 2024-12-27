import tkinter as tk
from tkinter import messagebox
import requests

def fetch_german_companies():
    response = requests.get("https://api.example.com/german_companies")
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", "Failed to fetch German companies")
        return []

def create_german_companies_window(app, stock_entry):
    german_companies_window = tk.Toplevel(app)
    german_companies_window.title("German Companies")

    def on_company_select(event):
        selected_company = company_listbox.get(company_listbox.curselection())
        stock_entry.delete(0, tk.END)
        stock_entry.insert(0, selected_company)

    german_companies = fetch_german_companies()

    tk.Label(german_companies_window, text="Select a German Company:").pack()
    company_listbox = tk.Listbox(german_companies_window)
    company_listbox.pack()
    for company in german_companies:
        company_listbox.insert(tk.END, company)
    company_listbox.bind("<<ListboxSelect>>", on_company_select)
