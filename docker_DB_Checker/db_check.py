from pathlib import Path
import sqlite3
from datetime import datetime

# Database stored inside mounted volume
db_path = Path("/data/local_database.db")

print(f"Using database: {db_path}")

# Connect creates the DB file automatically if it doesn't exist
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT,
    created_at TEXT
)
""")

# Insert one row
cursor.execute(
    "INSERT INTO logs (message, created_at) VALUES (?, ?)",
    ("Hello from Docker + SQLite", str(datetime.now()))
)

conn.commit()

# Read all rows
cursor.execute("SELECT * FROM books")

rows = cursor.fetchall()

print("\nCurrent rows:")

for row in rows:
    print(row)

conn.close()