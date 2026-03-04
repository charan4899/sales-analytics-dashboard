import sqlite3

def create_database():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            region TEXT,
            revenue REAL,
            month TEXT
        )
    """)

    # Insert sample data
    sample_data = [
        ("Laptop", "North", 12000, "January"),
        ("Phone", "South", 8000, "January"),
        ("Tablet", "East", 6000, "January"),
        ("Laptop", "West", 15000, "February"),
        ("Phone", "North", 9000, "February"),
        ("Tablet", "South", 7000, "February"),
    ]

    cursor.executemany("""
        INSERT INTO sales (product_name, region, revenue, month)
        VALUES (?, ?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created and sample data inserted!")