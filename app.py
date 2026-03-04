from flask import Flask, render_template, request, redirect
import csv
import sqlite3

app = Flask(__name__)

# ✅ Month ordering logic (Reusable)
MONTH_ORDER = """
    CASE month
        WHEN 'January' THEN 1
        WHEN 'February' THEN 2
        WHEN 'March' THEN 3
        WHEN 'April' THEN 4
        WHEN 'May' THEN 5
        WHEN 'June' THEN 6
        WHEN 'July' THEN 7
        WHEN 'August' THEN 8
        WHEN 'September' THEN 9
        WHEN 'October' THEN 10
        WHEN 'November' THEN 11
        WHEN 'December' THEN 12
    END
"""

@app.route('/')
def home():
    selected_region = request.args.get('region')

    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    if selected_region:
        query_filter = "WHERE region = ?"

        cursor.execute(f"SELECT SUM(revenue) FROM sales {query_filter}", (selected_region,))
        total_revenue = cursor.fetchone()[0]

        cursor.execute(f"""
            SELECT product_name, SUM(revenue) as total
            FROM sales {query_filter}
            GROUP BY product_name
            ORDER BY total DESC
            LIMIT 1
        """, (selected_region,))
        result = cursor.fetchone()
        top_product = result[0] if result else "N/A"

        cursor.execute(f"""
            SELECT month, SUM(revenue) as total
            FROM sales {query_filter}
            GROUP BY month
            ORDER BY {MONTH_ORDER}
        """, (selected_region,))
        monthly_data = cursor.fetchall()

    else:
        cursor.execute("SELECT SUM(revenue) FROM sales")
        total_revenue = cursor.fetchone()[0]

        cursor.execute("""
            SELECT product_name, SUM(revenue) as total
            FROM sales
            GROUP BY product_name
            ORDER BY total DESC
            LIMIT 1
        """)
        top_product = cursor.fetchone()[0]

        cursor.execute(f"""
            SELECT month, SUM(revenue) as total
            FROM sales
            GROUP BY month
            ORDER BY {MONTH_ORDER}
        """)
        monthly_data = cursor.fetchall()

    conn.close()

    # Growth calculation (based on ordered months)
    if len(monthly_data) >= 2:
        first = monthly_data[0][1]
        second = monthly_data[1][1]
        growth = ((second - first) / first) * 100 if first != 0 else 0
    else:
        growth = 0

    return render_template(
        "index.html",
        total_revenue=total_revenue,
        top_product=top_product,
        growth=round(growth, 2),
        monthly_data=monthly_data,
        selected_region=selected_region
    )

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file:
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()

        csv_reader = csv.reader(file.read().decode('utf-8').splitlines())
        next(csv_reader)

        for row in csv_reader:
            product_name, region, revenue, month = row
            cursor.execute("""
                INSERT INTO sales (product_name, region, revenue, month)
                VALUES (?, ?, ?, ?)
            """, (product_name, region, float(revenue), month))

        conn.commit()
        conn.close()

    return redirect('/')

@app.route('/api/monthly-data')
def api_monthly_data():
    selected_region = request.args.get('region')

    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    if selected_region:
        cursor.execute(f"""
            SELECT month, SUM(revenue) as total
            FROM sales
            WHERE region = ?
            GROUP BY month
            ORDER BY {MONTH_ORDER}
        """, (selected_region,))
    else:
        cursor.execute(f"""
            SELECT month, SUM(revenue) as total
            FROM sales
            GROUP BY month
            ORDER BY {MONTH_ORDER}
        """)

    data = cursor.fetchall()
    conn.close()

    formatted = [
        {"month": row[0], "revenue": row[1]}
        for row in data
    ]

    return {"data": formatted}

@app.route('/reports')
def reports():
    return render_template("reports.html")

@app.route('/analytics')
def analytics():
    return render_template("analytics.html")

@app.route('/api/reports')
def api_reports():
    page = request.args.get('page', 1, type=int)
    limit = 10
    offset = (page - 1) * limit

    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM sales")
    total_records = cursor.fetchone()[0]

    cursor.execute("""
        SELECT product_name, region, revenue, month
        FROM sales
        LIMIT ? OFFSET ?
    """, (limit, offset))

    rows = cursor.fetchall()
    conn.close()

    data = [
        {
            "product_name": row[0],
            "region": row[1],
            "revenue": row[2],
            "month": row[3]
        }
        for row in rows
    ]

    return {
        "data": data,
        "total": total_records,
        "page": page,
        "total_pages": (total_records + limit - 1) // limit
    }

@app.route('/api/region-data')
def api_region_data():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT region, SUM(revenue) as total
        FROM sales
        GROUP BY region
        ORDER BY total DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    data = [
        {"region": row[0], "revenue": row[1]}
        for row in rows
    ]

    return {"data": data}

@app.route('/api/top-products')
def api_top_products():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT product_name, SUM(revenue) as total
        FROM sales
        GROUP BY product_name
        ORDER BY total DESC
        LIMIT 5
    """)

    rows = cursor.fetchall()
    conn.close()

    data = [
        {"product": row[0], "revenue": row[1]}
        for row in rows
    ]

    return {"data": data}

if __name__ == '__main__':
    app.run(debug=True)