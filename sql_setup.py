import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect("data/ecommerce.db")
    df = pd.read_csv("data/products.csv")
    df.to_sql("products", conn, if_exists="replace", index=False)
    conn.close()
    print("Database créée ✔️")

if __name__ == "__main__":
    init_db()

