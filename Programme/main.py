import streamlit as st
import pandas as pd
from data_handler import load_data, save_data

# Streamlit App
def run():
    st.set_page_config(page_title="Börsenprogramm", layout="wide")
    st.title("📈 Börsenprogramm – Aktienanalyse")

    # Daten laden
    df = load_data()

    # Neue Firma hinzufügen
    with st.sidebar:
        st.header("➕ Firma hinzufügen")
        name = st.text_input("Firmenname")
        kgv = st.number_input("KGV", min_value=0.0, step=0.1)
        dividende = st.number_input("Dividende (%)", min_value=0.0, step=0.1)
        
        if st.button("Hinzufügen"):
            if name and kgv >= 0 and dividende >= 0:
                bewertung = 100 - (kgv * 2) + (dividende * 5)
                new_data = pd.DataFrame([[name, kgv, dividende, bewertung]], 
                                        columns=["Name", "KGV", "Dividende", "Bewertung"])
                df = pd.concat([df, new_data], ignore_index=True)
                save_data(df)
                st.success(f"Firma '{name}' hinzugefügt!")
                st.experimental_rerun()

    # Tabelle anzeigen
    st.subheader("📊 Firmendaten")
    st.dataframe(df)

    # Top 5 Firmen nach Bewertung
    if not df.empty:
        st.subheader("🏆 Top 5 Firmen nach Bewertung")
        df_sorted = df.sort_values(by="Bewertung", ascending=False).head(5)
        st.bar_chart(df_sorted.set_index("Name")["Bewertung"])

if __name__ == "__main__":
    run()
