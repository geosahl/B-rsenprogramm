import pandas as pd

CSV_FILE = "firmen_daten.csv"

def load_data():
    try:
        return pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "KGV", "Dividende", "Bewertung"])

def save_data(df):
    df.to_csv(CSV_FILE, index=False)
