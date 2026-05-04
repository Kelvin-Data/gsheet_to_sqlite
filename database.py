import sqlite3

conn = sqlite3.connect('invoices.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    customer TEXT,
    address TEXT,
    email TEXT,
    description TEXT,
    rate REAL,
    quantity INTEGER,
    UNIQUE(timestamp, email)
)
""")
print("Database and table created (if not exists)")
