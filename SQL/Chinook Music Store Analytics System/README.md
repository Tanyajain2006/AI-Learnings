# Chinook Music Store Analytics System

## Project Overview

This project analyzes the Chinook SQLite database using SQL, Python, Pandas, and Matplotlib.

The Chinook database represents a digital music store containing:
- customers
- invoices
- tracks
- albums
- artists
- employees
- playlists

The goal of this project is to:
- practice SQL querying
- understand relational databases
- perform business analytics
- visualize insights using charts

---

# Technologies Used

- Python
- SQLite
- Pandas
- Matplotlib
- Jupyter Notebook

---

# Project Structure

```text
Chinook Music Store Analytics System/
│
├── data/
│   └── Chinook_Sqlite.sqlite
│
├── notebooks/
│   ├── Chinook_Analysis.ipynb
│   └── run_sql.py
│
├── queries/
│   ├── Album_schema.sql
│   ├── Artist_schema.sql
│   ├── Customer_schema.sql
│   ├── Invoice_schema.sql
│   ├── InvoiceLine_schema.sql
│   ├── Track_schema.sql
│   └── solutions_to_queries/
│       ├── Top_10_Tracks.sql
│       ├── Country_Most_Revenue.sql
│       └── Top_Performing_Employee.sql
│
├── visualizations/
│   ├── top_tracks.png
│   ├── country_revenue.png
│   └── top_sales_employee.png
│
├── requirements.txt
└── README.md

---

# Relationship Notes

Customer → Invoice
One customer can have multiple invoices.

Invoice → InvoiceLine
One invoice can contain multiple tracks.

Track → Album
Many tracks belong to one album.