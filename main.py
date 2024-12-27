import tkinter as tk
from tkinter import messagebox
import webbrowser
import yfinance as yf

def fetch_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    hist = stock.history(period="3mo")
    pe_ratio = stock.info['forwardPE']
    return hist, pe_ratio

def open_finance_net():
    webbrowser.open("https://www.finance.net")

def open_finanzenzero():
    webbrowser.open("https://www.finanzenzero.com")

def show_stock_data():
    stock_symbol = stock_entry.get()
    purchase_price = purchase_price_entry.get()
    if not stock_symbol:
        messagebox.showerror("Error", "Please enter a stock symbol")
        return
    hist, pe_ratio = fetch_stock_data(stock_symbol)
    data_text.delete(1.0, tk.END)
    data_text.insert(tk.END, f"Stock: {stock_symbol}\n")
    data_text.insert(tk.END, f"Purchase Price: {purchase_price}\n")
    data_text.insert(tk.END, f"P/E Ratio: {pe_ratio}\n")
    data_text.insert(tk.END, "Price Trend (Last 3 Months):\n")
    data_text.insert(tk.END, hist.to_string())

app = tk.Tk()
app.title("Börsenprogramm")

tk.Label(app, text="Enter Stock Symbol:").pack()
stock_entry = tk.Entry(app)
stock_entry.pack()

tk.Label(app, text="Enter Purchase Price:").pack()
purchase_price_entry = tk.Entry(app)
purchase_price_entry.pack()

tk.Button(app, text="Show Stock Data", command=show_stock_data).pack()
tk.Button(app, text="Open finance.net", command=open_finance_net).pack()
tk.Button(app, text="Open finanzenzero", command=open_finanzenzero).pack()

data_text = tk.Text(app)
data_text.pack()

app.mainloop()
