import sqlite3
import os
from sql_setup import init_db

def sql_answer(query: str):

    conn = sqlite3.connect("data/ecommerce.db")
    cursor = conn.cursor()

    query_lower = query.lower()

    if "stock" in query_lower:
        cursor.execute("SELECT * FROM products WHERE stock < 10")
        result = cursor.fetchall()

    elif "price" in query_lower:
        cursor.execute("SELECT name, price FROM products ORDER BY price DESC")
        result = cursor.fetchall()

    else:
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()

    conn.close()
    return "\n".join([str(r) for r in result])



if not os.path.exists("data/ecommerce.db"):
    init_db()