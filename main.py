import tkinter as tk
from tkinter import ttk, messagebox
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fetch_german_companies():
    print("Fetching list of German companies...")
    return ["SAP.DE", "SIE.DE", "VOW3.DE", "BMW.DE", "BAS.DE", "DBK.DE", "ALV.DE", "MBG.DE", "ADS.DE", "LHA.DE"]

def fetch_stock_data(company):
    try:
        print(f"Fetching data for {company}...")
        stock = yf.Ticker(company)
        stock_info = stock.info
        hist = stock.history(period="3mo")  # Fetch historical data for the last three months
        print(f"Data for {company} fetched successfully.")
        return {
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
            "History": hist['Close'].tolist()
        }
    except Exception as e:
        print(f"Failed to fetch data for {company}: {e}")
        messagebox.showerror("Error", f"Failed to fetch data for {company}: {e}")
        return None

def plot_stock_history(history):
    fig, ax = plt.subplots(figsize=(2, 1))
    ax.plot(history, color='blue')
    ax.set_xticks([])
    ax.set_yticks([])
    return fig

def show_stock_data():
    for company in companies:
        stock_data = fetch_stock_data(company)
        if stock_data:
            item_id = tree.insert("", "end", values=(
                company, stock_data["Name"], stock_data["KGV"], stock_data["Dividend Yield"], stock_data["Market Cap"],
                stock_data["Current Price"], stock_data["Bid"], stock_data["Ask"], stock_data["Beta"], stock_data["EPS"],
                stock_data["P/E Ratio"], stock_data["Sector"], stock_data["Industry"], stock_data["ISIN"], stock_data["WKN"], ""
            ))
            fig = plot_stock_history(stock_data["History"])
            canvas = FigureCanvasTkAgg(fig, master=tree)
            canvas.draw()
            tree.update_idletasks()  # Ensure the treeview is updated
            bbox = tree.bbox(item_id, column="Chart")
            if bbox:
                x, y, width, height = bbox
                canvas.get_tk_widget().place(x=x, y=y, width=width, height=height)

def sort_column(tree, col, reverse):
    data_list = [(tree.set(k, col), k) for k in tree.get_children('')]
    data_list.sort(reverse=reverse)
    for index, (val, k) in enumerate(data_list):
        tree.move(k, '', index)
    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

print("Starting the application...")
root = tk.Tk()
root.title("Börsenprogramm")

companies = fetch_german_companies()

# Create Treeview
print("Creating Treeview...")
columns = (
    "Symbol", "Name", "KGV", "Dividend Yield", "Market Cap", "Current Price", "Bid", "Ask", "Beta", "EPS",
    "P/E Ratio", "Sector", "Industry", "ISIN", "WKN", "Chart"
)
tree = ttk.Treeview(root, columns=columns, show="headings")
column_widths = {
    "Symbol": 100, "Name": 150, "KGV": 100, "Dividend Yield": 120, "Market Cap": 120, "Current Price": 120,
    "Bid": 100, "Ask": 100, "Beta": 100, "EPS": 100, "P/E Ratio": 100, "Sector": 150, "Industry": 150,
    "ISIN": 150, "WKN": 100, "Chart": 200
}
for col in columns:
    tree.heading(col, text=col, command=lambda _col=col: sort_column(tree, _col, False))
    tree.column(col, width=column_widths[col])
tree.pack(fill=tk.BOTH, expand=True)

# Fetch and display stock data immediately
print("Fetching and displaying stock data...")
show_stock_data()

print("Starting the Tkinter main loop...")
root.mainloop()