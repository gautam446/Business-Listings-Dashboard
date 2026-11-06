# Business Listings Dashboard

A Business Listings Dashboard built using React.js, FastAPI, and MySQL. It helps users explore business listings through city-wise and category-wise charts, summary cards, and a searchable business table.

## Tech Stack

**Frontend**
- React.js
- Vite
- Recharts
- CSS

**Backend**
- Python
- FastAPI
- SQLAlchemy
- PyMySQL

**Database**
- MySQL

## Features

- Dashboard with total listing statistics.
- City-wise business listing chart.
- Category-wise pie chart.
- Source-wise listing summary.
- Search businesses by name, category, or city.
- Bulk insert API.
- MySQL database integration.

## Project Structure

```text
Business-Listings-Dashboard/
├── backend/
│   ├── app/
│   ├── scraper/
│   ├── scripts/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   └── package.json
├── database/
│   ├── listing_master.sql
│   └── business_dashboard.sql
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/gautam446/Business-Listings-Dashboard.git
cd Business-Listings-Dashboard
```

### 2. Database Setup

Create a MySQL database:

```sql
CREATE DATABASE business_dashboard;
```

Import the SQL file:

```bash
mysql -u root -p business_dashboard < database/business_dashboard.sql
```

### 3. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install cryptography
```

Create a `.env` file using `.env.example` and configure your MySQL connection.

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

API Documentation:

http://127.0.0.1:8000/docs

### 4. Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open:

http://localhost:5173

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /api/listings/bulk | Insert multiple listings |
| GET | /api/listings | Get business listings |
| GET | /api/dashboard/summary | Dashboard summary |
| GET | /api/dashboard/city-wise | City-wise statistics |
| GET | /api/dashboard/category-wise | Category-wise statistics |
| GET | /api/dashboard/source-wise | Source-wise statistics |

## Data Collection

This project currently includes 600 synthetic demo records generated for testing the dashboard and database functionality.

These records are not real businesses and have not been scraped from Google Maps, Justdial, or other business directories.

A basic HTML scraper is included for static HTML pages that the user owns or has permission to scrape. Actual real-world data collection is not included in the current demo dataset.

## Challenges

- Connecting FastAPI with MySQL.
- Configuring MySQL authentication.
- Integrating React with FastAPI.
- Displaying database statistics using charts.
- Implementing business listing search.

## Future Improvements

- Collect real business listings from permitted sources.
- Add pagination and advanced filters.
- Improve data validation.
- Deploy the application online.

## Author

Gautam Parmar

GitHub: https://github.com/gautam446
