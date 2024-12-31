import tkinter as tk
from tkinter import ttk
import requests

def fetch_german_companies():
    # Placeholder function to fetch the list of German companies from an API
    return ["SAP", "Siemens", "Volkswagen", "BMW", "BASF", "Deutsche Bank", "Allianz", "Daimler", "Adidas", "Lufthansa"]

def show_company_data(company):
    # Placeholder function to fetch and display stock data for the selected company
    print(f"Displaying data for {company}")

def open_german_companies_window():
    german_companies_window = tk.Toplevel()
    german_companies_window.title("German Companies")

    companies = fetch_german_companies()
    selected_company = tk.StringVar()
    selected_company.set(companies[0])

    company_dropdown = ttk.Combobox(german_companies_window, textvariable=selected_company, values=companies)
    company_dropdown.pack()

    show_data_button = tk.Button(german_companies_window, text="Show Company Data", command=lambda: show_company_data(selected_company.get()))
    show_data_button.pack()
