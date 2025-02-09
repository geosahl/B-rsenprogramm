import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import tkinter as tk
import os

# Liste der Unternehmen
companies = ["SAP.DE", "SIE.DE", "VOW3.DE", "BMW.DE", "BAS.DE", "DBK.DE", "ALV.DE", "MBG.DE", "ADS.DE", "LHA.DE"]

def fetch_stock_data(symbol):
    """
    Ruft die historischen Daten für die letzten 3 Monate ab.
    """
    stock = yf.Ticker(symbol)
    hist = stock.history(period="3mo")
    return hist

def fetch_logo(symbol):
    """
    Lade das Logo aus dem lokalen Ordner 'C:/Boersenprogramm/Logos', 
    wobei die Dateinamen ohne .DE (o.ä.) gespeichert sind.
    """
    try:
        symbol_clean = symbol.split(".")[0]
        dateipfad = os.path.join("C:/Boersenprogramm/Logos", f"{symbol_clean}.png")
        img = Image.open(dateipfad)
        return img
    except Exception as e:
        print(f"Failed to load local logo for '{symbol}': {e}")
        return None

def plot_stock_history(ax, symbol):
    """
    Erstellt ein Diagramm der Schlusskurse der letzten 3 Monate und zeigt das Firmenlogo an.
    """
    hist = fetch_stock_data(symbol)
    logo = fetch_logo(symbol)
    
    ax.plot(hist.index, hist['Close'], label=symbol)
    ax.set_title(f'Schlusskurse der letzten 3 Monate für {symbol}', fontsize=12)
    ax.set_xlabel('Datum', fontsize=10)
    ax.set_ylabel('Schlusskurs', fontsize=10)
    ax.legend()
    ax.grid(True)
    
    if logo:
        # Logo anzeigen
        imagebox = OffsetImage(logo, zoom=0.05)
        ab = AnnotationBbox(imagebox, (0.95, 0.95), frameon=False, xycoords='axes fraction')
        ax.add_artist(ab)

def create_charts_window(companies):
    """
    Erstellt ein Fenster mit einem Diagramm für jede Firma.
    """
    root = tk.Tk()
    root.title("Aktienkurse der letzten 3 Monate")

    rows = len(companies)
    subplot_height = 4  # Feste Höhe pro Diagramm
    extra_space = 1.0  # Zeilenabstand

    # Höhe der Figur berechnen
    fig_height = rows * subplot_height + (rows - 1) * extra_space
    fig, axs = plt.subplots(rows, 1, figsize=(10, fig_height), squeeze=False)
    fig.subplots_adjust(hspace=extra_space)  # Zeilenabstand einstellen
    axs = axs.flatten()

    # Diagramme plotten
    for ax, company in zip(axs, companies):
        plot_stock_history(ax, company)
        ax.set_title(f"Schlusskurse der letzten 3 Monate für {company}", fontsize=12)
        ax.set_xlabel("Datum", fontsize=10)
        ax.set_ylabel("Schlusskurs", fontsize=10)
        ax.tick_params(axis='x', labelrotation=45)  # Lesbare Beschriftungen

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    create_charts_window(companies)