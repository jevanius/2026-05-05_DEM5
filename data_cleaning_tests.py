import unittest
import data_cleaning
import pandas as pd
from datetime import datetime

class TestOperations(unittest.TestCase):
    
    def setUp(self):
        self.csv_content = pd.DataFrame([
    {
        "Id": float(1),
        "Books": "Catcher in the Rye",
        "Book checkout": "\"23/04/2024\"",
        "Book Returned": "25/04/2024",
        "Days allowed to borrow": "2 weeks",
        "Customer ID": float(1)
    }])
        self.corrected_data = pd.DataFrame([
    {
        "Id": float(1),
        "Books": "Catcher in the Rye",
        "Book checkout": datetime(2024, 4, 23),
        "Book Returned": datetime(2024, 4, 25),
        "Days allowed to borrow": "2 weeks",
        "Customer ID": float(1),
        "loan_duration": float(2),
        "overdue": "no"
    }])

        self.df = data_cleaning.load_csv("test_csv.csv")     
    
    
    def test_load(self):
        pd.testing.assert_frame_equal(self.csv_content,self.df.iloc[[0]])
    
    def test_fix_dates(self):
        df = data_cleaning.fix_dates(self.df)
        pd.testing.assert_frame_equal(self.corrected_data.drop(columns=["overdue","loan_duration"]),self.df.iloc[[0]])


    def test_fix_na(self):
        df = data_cleaning.fix_dates(self.df)
        df = data_cleaning.fix_na(df)
        pd.testing.assert_frame_equal(self.corrected_data.drop(columns=["overdue","loan_duration"]),df)


    def test_validate_loans(self):
        df = data_cleaning.fix_dates(self.df)
        df = data_cleaning.validate_loans('Book Returned','Book checkout',df)
        pd.testing.assert_frame_equal(self.corrected_data.drop(columns=["overdue"]),df.iloc[[0]])


    def test_overdue_check(self):
        df = data_cleaning.fix_dates(self.df)
        df = data_cleaning.validate_loans('Book Returned','Book checkout',df)
        df = data_cleaning.overdue_check(df)
        pd.testing.assert_frame_equal(self.corrected_data,df.iloc[[0]])



if __name__ == "__main__":
    unittest.main()