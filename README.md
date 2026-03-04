# 📊 Sales Analytics Dashboard

A full-stack **Sales Analytics Platform** built using **Flask** and **SQLite**, designed to simulate a real-world business intelligence and reporting system.

This project demonstrates backend API engineering, SQL aggregation logic, REST architecture design, CSV ingestion pipelines, pagination, and frontend visualization using Chart.js.

---

## 🚀 Project Overview

The application allows users to:

- Upload raw CSV sales datasets
- Store and normalize data into a SQLite database
- Perform SQL-based revenue aggregations
- Filter analytics by region
- Identify top-performing products
- Generate paginated sales reports
- Visualize results using interactive charts

It simulates how internal BI dashboards are built in real-world companies.

---

## 🏗 System Architecture

```
Frontend (HTML, CSS, JavaScript)
        ↓
Flask REST API (app.py)
        ↓
SQLite Database (sales.db)
        ↓
SQL Aggregations & Query Processing
```

---

## 🛠 Tech Stack

- Python
- Flask
- SQLite
- SQL (GROUP BY, ORDER BY, LIMIT, OFFSET)
- HTML / CSS / JavaScript
- REST APIs
- Chart.js (Visualization)
- CSV Processing (Python csv module)

---

## 📂 Project Structure

```
sales-analytics-dashboard/
│
├── app.py
├── sales.db
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── uploads/
├── requirements.txt
└── README.md
```

---

## 🗄 Database Schema

### Table: `sales`

| Column Name  | Type |
|-------------|------|
| product_name | TEXT |
| region       | TEXT |
| revenue      | REAL |

> Data is populated dynamically from uploaded CSV files.

---

## 📁 CSV Data Ingestion Flow

1. User uploads a CSV file.
2. Flask parses the file using Python’s CSV module.
3. Data is inserted into the `sales` table.
4. SQL queries power analytics endpoints.

This mimics ETL-style data ingestion used in analytics systems.

---

## 🔌 REST API Endpoints

### 1️⃣ Monthly Revenue Aggregation

```
GET /api/monthly-data
```

**Functionality:**
- Groups sales by month
- Uses SQL `GROUP BY`
- Orders months chronologically using custom month ordering logic

---

### 2️⃣ Region-Based Revenue

```
GET /api/region-data
```

- Aggregates revenue by region
- Enables region-based filtering from frontend

---

### 3️⃣ Top Products

```
GET /api/top-products
```

- Identifies highest revenue-generating products
- Uses `GROUP BY` + `ORDER BY DESC`
- Limited results using `LIMIT`

---

### 4️⃣ Paginated Sales Reports

```
GET /api/reports?page=1
```

- Implements pagination
- Uses `LIMIT` and `OFFSET`
- Designed for scalable data retrieval


---

## 📊 Frontend Visualization

- Chart.js used for:
  - Monthly revenue bar charts
  - Region-wise pie charts
  - Top products leaderboard
- Data fetched asynchronously via REST APIs (AJAX)

---

## ✨ Key Features

- CSV Sales Data Upload
- Revenue Aggregation by Month
- Chronological Month Ordering Logic
- Region-Based Filtering
- Top Product Identification
- Paginated Reports
- Interactive Charts
- Modular Backend Structure
- RESTful API Design

---

## 📚 Technical Learning Outcomes

- Implemented SQL aggregation with dynamic filtering
- Designed paginated REST API endpoints
- Built data ingestion workflow
- Integrated backend data with frontend visualization
- Applied query optimization techniques
- Structured scalable Flask backend architecture
- Simulated real-world BI dashboard development

---

## 🔮 Future Enhancements

- PostgreSQL Migration
- User Authentication System
- Role-Based Access Control
- Revenue Forecasting (ML Integration)
- Dockerized Deployment
- Cloud Hosting (AWS / Render / Railway)

---


## 📄 License

This project is open-source under the MIT License.
