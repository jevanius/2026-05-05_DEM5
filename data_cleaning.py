import pandas as pd
import os
import csv
import datetime as dt
import pyodbc
from sqlalchemy import create_engine


files = os.listdir("C:/Users/Admin/Downloads/data")

def fix_dates(data):
    if "Book checkout" in data.columns:
        data["Book checkout"]=data["Book checkout"].astype(str).str.strip().str.replace('"', '', regex=False)
        data["Book checkout"]=pd.to_datetime(data["Book checkout"],format="%d/%m/%Y",dayfirst=True,errors="coerce")    
        data["Book Returned"] = pd.to_datetime(data["Book Returned"],format="%d/%m/%Y",dayfirst=True,errors="coerce")
    return data

def load_csv(filepath):
    folder = ("C:/Users/Admin/Downloads/data/")
    data=pd.DataFrame()
    data = pd.read_csv(folder+filepath)
    return data

def fix_na(data):
    data = data.dropna(how='all') #drop rows where every value is NaN
    if "Books" in data.columns:
        data["Books"]=data["Books"].fillna("Unknown")
        data["Customer ID"]=data["Customer ID"].fillna(999)
    return data

def save_clean(data):
    filename = f.replace(".csv","")
    data.to_csv('C:/Users/Admin/Documents/2026-05-05_DEM5/data/'+filename+'_clean.csv', index = False)

def validate_loans(returnCol,checkoutCol,data):
    data['loan_duration'] = (data[returnCol]-data[checkoutCol]).dt.days
    data = data[data['loan_duration']>=0]
    return data

def overdue_check(data):
    data['overdue'] = data['loan_duration'].astype(int).apply(lambda x: 'yes' if x > 14 else 'no')
    return data

for f in files:
    print("converting "+ f)
    table = load_csv(f)
    table = fix_dates(table)
    table = fix_na(table)
    if "Books" in table.columns:
        table = validate_loans('Book Returned','Book checkout',table)
        overdue_check(table)
    save_clean(table)
    