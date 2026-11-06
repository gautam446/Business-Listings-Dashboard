# Business Listings Dashboard

A beginner-friendly full-stack assignment project using **React + FastAPI + MySQL**.

## Features
- FastAPI backend connected to MySQL with SQLAlchemy.
- `listing_master` table.
- Bulk insert API.
- City-wise, category-wise, and source-wise dashboard APIs.
- React dashboard with summary cards, Recharts charts, and a searchable listings table.
- A sample-data generator that inserts 600 clearly labelled demo records.
- An optional HTML scraper for pages you own or are explicitly allowed to scrape.

> **Important about the data:** The included 600 records are synthetic demo/sample data, not real scraped businesses. The assignment brief allows mock/sample data when scraping is blocked, provided the approach is explained. Do not describe these demo records as real scraped data. Before scraping a third-party directory, check its terms, robots.txt, and permission requirements. Do not bypass logins, CAPTCHAs, or access controls.

## Project structure

```text
Business-Listings-Dashboard/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── main.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── listings.py
│   ├── scraper/
│   │   └── html_scraper.py
│   ├── scripts/
│   │   └── generate_sample_data.py
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── api.js
│       └── style.css
├── database/
│   └── listing_master.sql
├── .gitignore
└── README.md
```

## 1. Install prerequisites
Install:
- Python 3.10 or newer
- Node.js LTS
- MySQL Server (MySQL Workbench is optional)

## 2. Create the MySQL database
Open MySQL Workbench or the MySQL command line and run the SQL in `database/listing_master.sql`.

The SQL creates a database named `business_dashboard` and a table named `listing_master`.

## 3. Configure backend
Open a terminal in the `backend` folder.

Windows:
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` and set your own MySQL username and password:
```env
DATABASE_URL=mysql+pymysql://root:YOUR_MYSQL_PASSWORD@localhost:3306/business_dashboard
```
If your MySQL root account has no password, leave the password section empty:
`mysql+pymysql://root:@localhost:3306/business_dashboard`

Start backend:
```powershell
uvicorn app.main:app --reload
```

Backend:
- API: http://127.0.0.1:8000
- Interactive API docs: http://127.0.0.1:8000/docs

The app creates the table automatically if the database already exists.

## 4. Add 600 demo listings
Open a second terminal in `backend`, activate the virtual environment, then run:
```powershell
python -m scripts.generate_sample_data
```
This inserts 600 synthetic demo records. It avoids duplicates by checking the demo source and clears earlier demo rows before inserting a fresh set.

## 5. Start frontend
Open another terminal in the `frontend` folder:
```powershell
npm install
npm run dev
```
Open the local URL shown by Vite, usually http://localhost:5173.

## API endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Backend status |
| POST | `/api/listings/bulk` | Insert a list of listings |
| GET | `/api/listings` | Get listings with search and pagination |
| GET | `/api/dashboard/summary` | Total listings, cities, categories, sources |
| GET | `/api/dashboard/city-wise` | City-wise counts |
| GET | `/api/dashboard/category-wise` | Category-wise counts |
| GET | `/api/dashboard/source-wise` | Source-wise counts |

Example bulk insert body:
```json
[
  {
    "business_name": "Example Computer Center",
    "category": "Computer Training",
    "city": "Ahmedabad",
    "address": "CG Road, Ahmedabad",
    "phone": "9999999999",
    "source": "Permitted HTML source"
  }
]
```

## Optional HTML scraping
`backend/scraper/html_scraper.py` is a simple scraper for **static HTML pages that you own or have permission to collect data from**. It uses CSS selectors you provide. It is not a universal scraper and will not automatically work on every directory website.

Example:
```powershell
python -m scraper.html_scraper --url "https://your-authorized-directory.example/listings" --name-selector ".business-name" --category-selector ".business-category" --city-selector ".business-city" --address-selector ".business-address" --phone-selector ".business-phone" --output listings.csv
```
Install backend requirements first. Review the target site's terms and robots.txt before using it. Some sites load listings with JavaScript or prohibit automated collection; do not try to evade those restrictions.

## Database dump
The starter SQL schema is in `database/listing_master.sql`. After inserting data, you can export the actual database using MySQL Workbench (Server > Data Export) or:
```bash
mysqldump -u root -p business_dashboard > database/business_dashboard_dump.sql
```
The generated dump contains your local database records, so do not commit it if it includes personal or restricted information.

## Demo video (3–5 minutes)
Suggested order:
1. Explain React, FastAPI, and MySQL architecture.
2. Show the sample-data note and explain why sample data is used if live scraping is blocked.
3. Show `/docs` and test the bulk insert and dashboard endpoints.
4. Show the dashboard cards, charts, and search table.
5. Explain setup steps and one challenge you faced.

## Challenges section (edit this with your real experience)
- Some business directories use dynamic pages or restrict automated scraping.
- Data may contain missing phone numbers or duplicate listings.
- The dashboard needs consistent city/category/source values for useful charts.
- MySQL credentials and local setup differ between computers.

## Before submission
- Replace demo records with permitted, verifiable data if you can lawfully obtain it.
- Test every API and the React dashboard on your own computer.
- Update this README with your actual screenshots, data source, and challenges.
- Push the repository to GitHub.
