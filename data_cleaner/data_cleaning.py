import pandas as pd
import os
import csv
import datetime as dt
import sqlite3


files = os.listdir("./data")

def fix_dates(data):
    if "Book checkout" in data.columns:
        data["Book checkout"]=data["Book checkout"].astype(str).str.strip().str.replace('"', '', regex=False)
        data["Book checkout"]=pd.to_datetime(data["Book checkout"],format="%d/%m/%Y",dayfirst=True,errors="coerce")    
        data["Book Returned"] = pd.to_datetime(data["Book Returned"],format="%d/%m/%Y",dayfirst=True,errors="coerce")
    return data

def load_csv(filepath):
    folder = ("./data/")
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
    data.to_csv('./data_clean/'+filename+'_clean.csv', index = False)

def validate_loans(returnCol,checkoutCol,data):
    data['loan_duration'] = (data[returnCol]-data[checkoutCol]).dt.days
    data = data[data['loan_duration']>=0]
    return data

def overdue_check(data):
    data['overdue'] = data['loan_duration'].astype(int).apply(lambda x: 'yes' if x > 14 else 'no')
    return data

def start_local_db(db_name="/data/local_database.db"):
   
    try:
        # Connect to SQLite database (creates file if it doesn't exist)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        print(f"Connected to database: {os.path.abspath(db_name)}")
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None, None

def read_data(db_name="/data/local_database.db"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT * FROM "+tablename, conn)
    print(df)
    conn.close()

def full_clean(table):
        table = load_csv(f)
        table = fix_dates(table)
        table = fix_na(table)
        if "Books" in table.columns:
            table = validate_loans('Book Returned','Book checkout',table)
            overdue_check(table)
        #print(table)
        return table

    #save_clean(table)

if __name__ == "__main__":
    #conn, cursor = start_local_db()
    for f in files:
        print("converting "+ f)
        table = full_clean(f)
        tablename = f.replace(".csv","")
        print("Saving "+tablename+"...")
        save_clean(table)
        #table.to_sql(tablename, conn, if_exists="replace", index=False)
        #read_data()
    #conn.close()
    