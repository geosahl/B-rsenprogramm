import tkinter as tk
import subprocess

def add_company():
    # Firmen aufnehmen.py öffnen
    subprocess.Popen(["python", "ui/add_company.py"])

def update_data():
    # Überblick.py öffnen
    subprocess.Popen(["python", "ui/analysis_page.py"])

def view_charts():
    # Charts.py öffnen
    subprocess.Popen(["python", "ui/csv_viewer.py"])

def create_start_page():
    root = tk.Tk()
    root.title("Startseite")

    # Fenstergröße festlegen
    root.geometry("300x200")

    # Buttons erstellen
    btn_add_company = tk.Button(root, text="Firma aufnehmen", command=add_company)
    btn_update_data = tk.Button(root, text="Daten aktualisieren", command=update_data)
    btn_view_charts = tk.Button(root, text="Charts schauen", command=view_charts)

    # Buttons platzieren
    btn_add_company.pack(pady=10)
    btn_update_data.pack(pady=10)
    btn_view_charts.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_start_page()