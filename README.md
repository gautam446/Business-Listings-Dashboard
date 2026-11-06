# Business Listings Dashboard

A full-stack web application to collect, store, manage, and visualize business listing data from OpenStreetMap using FastAPI, MySQL, React.js, and Recharts.

## 🚀 Project Overview

The Business Listings Dashboard provides a centralized platform to manage business listing records across different cities and categories.

It includes:
- Business listing data collection using OpenStreetMap.
- FastAPI backend for REST API operations.
- MySQL database for storing business records.
- React.js frontend for displaying business listings.
- Interactive charts for data visualization.
- Search and filtering functionality.

## 🛠️ Technology Stack

### Frontend
- React.js
- Vite
- Recharts
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- SQLAlchemy
- Uvicorn
- Requests

### Database
- MySQL 8.4

### Data Source
- OpenStreetMap (OSM)
- Overpass API

## 📊 Data Collection

Business listing records are collected from OpenStreetMap using the Overpass API.

The Python import script retrieves available map features with business-related tags, including:

- Shop
- Amenity
- Office
- Tourism
- Craft

### Current Dataset

| Details | Information |
|---|---|
| Data Source | OpenStreetMap |
| Total Imported Records | 4,482 |
| Database | MySQL |
| Database Table | listing_master |
| Cities | Ahmedabad, Surat |
| Import Script | backend/scripts/import_osm_data.py |

**Note:** The 4,482 records represent imported OpenStreetMap map features. Not every record necessarily contains a phone number or complete address. The dataset has not been independently verified as a complete list of active businesses.

## 📁 Project Structure

```text
Business-Listings-Dashboard/
│
├── backend/
│   ├── app/
│   ├── scripts/
│   │   ├── generate_sample_data.py
│   │   └── import_osm_data.py
│   ├── .env.example
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── index.html
│
├── database/
│   └── business_dashboard.sql
│
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/gautam446/Business-Listings-Dashboard.git
cd Business-Listings-Dashboard
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
```

Activate virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Database Configuration

Create a MySQL database:

```sql
CREATE DATABASE business_dashboard;
```

Import the database backup:

```bash
mysql -u root -p business_dashboard < database/business_dashboard.sql
```

Configure your database connection in the backend `.env` file using the provided `.env.example` as a reference.

### 4. Run Backend

From the backend directory:

```bash
uvicorn app.main:app --reload
```

Backend API:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

### 5. Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

## 📈 Dashboard Features

- Business listing management
- City-wise business statistics
- Category-wise statistics
- Source-wise statistics
- Interactive Bar Charts
- Interactive Pie Charts
- Business search and filtering
- REST API integration

## 🔌 API Features

The FastAPI backend provides endpoints for:

- Bulk inserting business records
- Retrieving business listings
- Dashboard statistics
- City-wise counts
- Category-wise counts
- Source-wise counts

Visit `/docs` to explore available API endpoints.

## 🌍 OpenStreetMap Attribution

This project uses data from OpenStreetMap contributors.

© OpenStreetMap contributors.

OpenStreetMap data is available under the Open Database License (ODbL).

Data source: https://www.openstreetmap.org/

Overpass API: https://overpass-api.de/

## ⚠️ Data Disclaimer

OpenStreetMap data is community-maintained and may contain incomplete, outdated, or missing information.

The imported records are presented as available in OpenStreetMap. No independent verification of every business listing has been performed.

## 👨‍💻 Developer

**Gautam Parmar**

GitHub: https://github.com/gautam446

## 📄 License

This project is developed for educational and internship assignment purposes.
