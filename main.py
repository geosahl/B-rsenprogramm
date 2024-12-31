import tkinter as tk
from tkinter import ttk
import requests

def fetch_german_companies():
    return ["SAP", "Siemens", "Volkswagen", "BMW", "BASF", "Deutsche Bank", "Allianz", "Daimler", "Adidas", "Lufthansa"]

def fetch_stock_data(company):
    # Placeholder function to fetch stock data for the selected company
    return {
        "KGV": 15.2,
        "Dividend Yield": 2.5,
        "Market Cap": "100B",
        "Stock Trend": [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155]
    }

def display_stock_data(stock_data):
    # Placeholder function to display stock data in a tabular format
    print("Displaying stock data:")
    for key, value in stock_data.items():
        print(f"{key}: {value}")

def show_stock_data():
    selected_company = company_dropdown.get()
    stock_data = fetch_stock_data(selected_company)
    display_stock_data(stock_data)

root = tk.Tk()
root.title("Börsenprogramm")

companies = fetch_german_companies()
company_dropdown = ttk.Combobox(root, values=companies)
company_dropdown.pack()

show_data_button = tk.Button(root, text="Show Stock Data", command=show_stock_data)
show_data_button.pack()

# Add a section to display stock data for 10 big German companies in a tabular format
stock_data_frame = ttk.Frame(root)
stock_data_frame.pack()

for company in companies:
    stock_data = fetch_stock_data(company)
    ttk.Label(stock_data_frame, text=f"{company}:").pack()
    for key, value in stock_data.items():
        ttk.Label(stock_data_frame, text=f"{key}: {value}").pack()

root.mainloop()
