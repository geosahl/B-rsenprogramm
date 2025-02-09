import requests
from config import API_KEY_FINANCIAL

BASE_URL = "https://financialmodelingprep.com/api/v3"

def get_stock_data(symbol):
    url = f"{BASE_URL}/profile/{symbol}?apikey={API_KEY_FINANCIAL}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None