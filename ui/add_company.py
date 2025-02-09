import tkinter as tk
from tkinter import simpledialog
import pandas as pd
from data_handler import load_data, save_data

def add_company():
    root = tk.Tk()
    root.withdraw()  # Versteckt das Hauptfenster

    name = simpledialog.askstring("Firma aufnehmen", "Name der Firma:")
    kgv = simpledialog.askfloat("Firma aufnehmen", "KGV:")
    dividende = simpledialog.askfloat("Firma aufnehmen", "Dividende:")
    ex_date = simpledialog.askstring("Firma aufnehmen", "Ex-Datum:")

    if name and kgv and dividende and ex_date:
        df = load_data()
        df = df.append({"Name": name, "KGV": kgv, "Dividende": dividende, "ExDate": ex_date, "Bewertung": None}, ignore_index=True)
        save_data(df)
        tk.messagebox.showinfo("Erfolg", "Firma erfolgreich aufgenommen!")
    else:
        tk.messagebox.showwarning("Fehler", "Alle Felder müssen ausgefüllt werden!")

if __name__ == "__main__":
    add_company()