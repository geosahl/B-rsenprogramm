import tkinter as tk
from tkinter import ttk, messagebox
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import requests
import io
import os

def fetch_german_companies():
    print("Fetching list of German companies...")
    return ["SAP.DE", "SIE.DE", "VOW3.DE", "BMW.DE", "BAS.DE", "DBK.DE", "ALV.DE", "MBG.DE", "ADS.DE", "LHA.DE"]

logos = {}  # Referenzen für die Logo-Bilder, damit sie nicht vorzeitig gelöscht werden

def fetch_logo(symbol: str):
    """
    Lade das Logo aus dem lokalen Ordner 'C:/Boersenprogramm/Logos' anstatt aus dem Internet.
    """
    try:
        dateipfad = os.path.join("C:/Boersenprogramm/Logos", f"{symbol}.png")
        with open(dateipfad, 'rb') as file:
            bild_inhalt = file.read()
        img_data = Image.open(io.BytesIO(bild_inhalt))
        img_data = img_data.resize((20, 20), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img_data)
    except Exception as e:
        print(f"Failed to load local logo for '{symbol}': {e}")
        return None

def fetch_stock_data(company):
    try:
        print(f"Fetching data for {company}...")
        stock = yf.Ticker(company)
        hist = stock.history(period="3mo")
        stock_info = stock.info

        # Lokales Logo laden, nicht aus dem Internet
        logos[company] = fetch_logo(company)

        print(f"Data for {company} (WKN: {stock_info.get('wkn', 'N/A')}, ISIN: {stock_info.get('isin', 'N/A')}) fetched successfully.")
        return {
            "Logo": logos.get(company),
            "Name": stock_info.get("longName", "N/A"),
            "KGV": f"{stock_info.get('forwardPE', 'N/A'):.2f}" if stock_info.get('forwardPE') else "N/A",
            "Dividend Yield": f"{stock_info.get('dividendYield', 'N/A'):.2f}" if stock_info.get('dividendYield') else "N/A",
            "Market Cap": f"{stock_info.get('marketCap', 'N/A'):.2f}" if stock_info.get('marketCap') else "N/A",
            "Current Price": f"{stock_info.get('currentPrice', 'N/A'):.2f}" if stock_info.get('currentPrice') else "N/A",
            "Bid": f"{stock_info.get('bid', 'N/A'):.2f}" if stock_info.get('bid') else "N/A",
            "Ask": f"{stock_info.get('ask', 'N/A'):.2f}" if stock_info.get('ask') else "N/A",
            "Beta": f"{stock_info.get('beta', 'N/A'):.2f}" if stock_info.get('beta') else "N/A",
            "EPS": f"{stock_info.get('trailingEps', 'N/A'):.2f}" if stock_info.get('trailingEps') else "N/A",
            "P/E Ratio": f"{stock_info.get('trailingPE', 'N/A'):.2f}" if stock_info.get('trailingPE') else "N/A",
            "Sector": stock_info.get("sector", "N/A"),
            "Industry": stock_info.get("industry", "N/A"),
            "ISIN": stock_info.get("isin", "N/A"),
            "WKN": stock_info.get("wkn", "N/A"),
            "HistoryClose": hist["Close"].tolist()
        }
    except Exception as e:
        print(f"Failed to fetch data for {company}: {e}")
        messagebox.showerror("Error", f"Failed to fetch data for {company}: {e}")
        return None

def plot_stock_history(history_data):
    fig, ax = plt.subplots(figsize=(2, 1))
    ax.plot(history_data, color='blue', linewidth=1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("", fontsize=2)
    return fig

def show_stock_data():
    for company in companies:
        stock_data = fetch_stock_data(company)
        if stock_data:
            item_id = tree.insert(
                "",
                "end",
                values=(
                    stock_data["Logo"],
                    company,
                    stock_data["Name"],
                    stock_data["KGV"],
                    stock_data["Dividend Yield"],
                    stock_data["Market Cap"],
                    stock_data["Current Price"],
                    stock_data["Bid"],
                    stock_data["Ask"],
                    stock_data["Beta"],
                    stock_data["EPS"],
                    stock_data["P/E Ratio"],
                    stock_data["Sector"],
                    stock_data["Industry"],
                    stock_data["ISIN"],  # ISIN hier einfügen
                    stock_data["WKN"],   # WKN hier einfügen
                    ""  # Chart-Spalte
                )
            )
            fig = plot_stock_history(stock_data["HistoryClose"])
            canvas = FigureCanvasTkAgg(fig, master=tree)
            canvas.draw()
            tree.update_idletasks()
            bbox = tree.bbox(item_id, column="Chart")
            if bbox:
                x, y, w, h = bbox
                canvas.get_tk_widget().place(x=x, y=y, width=w, height=h)

def sort_column(treeview, col, reverse):
    data_list = [(treeview.set(k, col), k) for k in treeview.get_children('')]
    data_list.sort(reverse=reverse)
    for index, (val, k) in enumerate(data_list):
        treeview.move(k, '', index)
    treeview.heading(col, command=lambda: sort_column(treeview, col, not reverse))

print("Starting the application...")
root = tk.Tk()
root.title("Börsenprogramm")

companies = fetch_german_companies()

print("Creating Treeview...")
columns = (
    "Logo", "Symbol", "Name", "KGV", "Dividend Yield", "Market Cap", "Current Price",
    "Bid", "Ask", "Beta", "EPS", "P/E Ratio", "Sector", "Industry",
    "ISIN", "WKN", "Chart"
)
tree = ttk.Treeview(root, columns=columns, show="headings")

column_widths = {
    "Logo": 30,
    "Symbol": 90,
    "Name": 150,
    "KGV": 80,
    "Dividend Yield": 110,
    "Market Cap": 110,
    "Current Price": 110,
    "Bid": 60,
    "Ask": 60,
    "Beta": 80,
    "EPS": 80,
    "P/E Ratio": 80,
    "Sector": 120,
    "Industry": 150,
    "ISIN": 120,
    "WKN": 100,
    "Chart": 200
}

for col in columns:
    tree.heading(col, text=col, command=lambda _col=col: sort_column(tree, _col, False))
    tree.column(col, width=column_widths[col])

tree.pack(fill=tk.BOTH, expand=True)

print("Fetching and displaying stock data...")
show_stock_data()

print("Starting the Tkinter main loop...")
root.mainloop()