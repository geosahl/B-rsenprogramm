import unittest
from data_handler import load_data, save_data
import pandas as pd

class TestDataHandler(unittest.TestCase):
    def test_load_data(self):
        df = load_data()
        self.assertIsInstance(df, pd.DataFrame)

    def test_save_data(self):
        df = pd.DataFrame({"Name": ["Test"], "KGV": [10], "Dividende": [2], "ExDate": ["2025-01-01"], "Bewertung": [50]})
        save_data(df)
        loaded_df = load_data()
        self.assertEqual(len(loaded_df), 1)
        self.assertEqual(loaded_df.iloc[0]["Name"], "Test")

if __name__ == "__main__":
    unittest.main()