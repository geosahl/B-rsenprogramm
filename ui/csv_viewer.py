import streamlit as st
from data_handler import load_data

def run():
    st.title("CSV-Datei-Anzeige")
    df = load_data()
    st.table(df)

if __name__ == "__main__":
    run()