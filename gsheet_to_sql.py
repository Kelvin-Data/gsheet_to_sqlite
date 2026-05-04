import pygsheets
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

def copy_gsheet_to_sqlite():
    path = os.getenv("GSHEET_PATH")
    gc = pygsheets.authorize(service_account_file = path)
    sh = gc.open('Invoice_form')
    wk = sh.worksheet_by_title('Form_responses')
    data = wk.get_all_records()
    print(data)
    
    conn = sqlite3.connect('invoices.db')
    cursor = conn.cursor()
    
    inserted = 0
    
    for row in data:
        cursor.execute("""
        INSERT OR IGNORE INTO orders (
            timestamp, customer, address, email, description, rate, quantity
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            row["Timestamp"],
            row["Who is the customer?"],
            row["What is the address?"],
            row["What is the email address"],
            row["What is the description of the goods or services"],
            row["What is the rate?"],
            row["How much is the quantity?"]
        ))

        if cursor.rowcount > 0:
            inserted += 1

    conn.commit()
    conn.close()

    return inserted

copy_gsheet_to_sqlite()
