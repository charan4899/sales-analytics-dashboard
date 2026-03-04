# sales-analytics-dashboard
**Overview**

This project is a full-stack Sales Analytics Platform built using Flask and SQLite, designed to simulate a real-world business intelligence reporting system.
The application enables users to upload sales data, process it using SQL aggregations, and visualize key performance metrics through interactive dashboards and analytics reports.
It demonstrates backend API development, database design, data aggregation logic, and frontend visualization integration.

**Architecture**
Frontend (HTML, CSS, JS)<br/>
⬇
Flask REST API
⬇
SQLite Database
⬇
SQL Aggregations & Data Processing

**Tech Stack**

Python, Flask, SQLite, SQL, HTML / CSS / JavaScript, REST APIs, Chart.js (for visualization)

**Key Features**
CSV Sales Data Upload\n
Revenue Aggregation by Month
Region-Based Filtering
Top Product Identification
Paginated Sales Reports
Interactive Charts
REST API Endpoints for Analytics
Modular Backend Structure

**Database Schema**

Table: sales

Column	Type
product_name	TEXT
region	TEXT
revenue	REAL

**API Endpoints**

GET /api/monthly-data
GET /api/region-data
GET /api/top-products
GET /api/reports

**Learning Outcomes**

Implemented SQL aggregation logic with dynamic filtering
Designed paginated REST API endpoints
Integrated backend data with frontend visualization
Handled CSV ingestion and database population
Built reusable query logic for month ordering

**Future Enhancements**

PostgreSQL migration
User authentication system
Role-based access
Revenue forecasting (ML integration)
Dockerized deployment
month	TEXT


