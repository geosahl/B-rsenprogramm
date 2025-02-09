import streamlit as st
from data_handler import load_data

def run():
    st.title("Börsenprogramm")
    df = load_data()
    st.table(df)

if __name__ == "__main__":
    run()