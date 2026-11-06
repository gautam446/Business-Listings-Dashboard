import random
from app.database import SessionLocal
from app.models import Listing

business_types = {
    "Restaurant": ["Spice Garden", "City Cafe", "Food Corner", "Green Bowl"],
    "Healthcare": ["Care Clinic", "Life Hospital", "Health Point", "Wellness Center"],
    "Education": ["Bright Academy", "Knowledge Hub", "Smart Classes", "Future Institute"],
    "IT Services": ["Tech Solutions", "Digital Works", "Code Studio", "Web Experts"],
    "Retail": ["City Mart", "Style Store", "Daily Needs", "Smart Shopping"]
}

cities = {
    "Ahmedabad": ["CG Road", "Navrangpura", "Maninagar", "Satellite"],
    "Surat": ["Adajan", "Vesu", "Varachha", "City Light"],
    "Vadodara": ["Alkapuri", "Manjalpur", "Gotri", "Fatehgunj"],
    "Rajkot": ["Kalawad Road", "University Road", "Gondal Road", "Yagnik Road"],
    "Bhavnagar": ["Waghawadi Road", "Nirmal Nagar", "Kalanala", "Ghogha Circle"]
}

def main():
    random.seed(42)
    db = SessionLocal()
    try:
        # Remove only previous generated demo rows, not any other source.
        db.query(Listing).filter(Listing.source == "Demo Sample Data").delete()
        rows = []
        categories = list(business_types.keys())
        city_names = list(cities.keys())

        for number in range(1, 601):
            category = random.choice(categories)
            city = random.choice(city_names)
            business_base = random.choice(business_types[category])
            area = random.choice(cities[city])
            rows.append(Listing(
                business_name=f"{business_base} {number:03d}",
                category=category,
                city=city,
                address=f"{area}, {city}, Gujarat",
                phone=f"9{random.randint(100000000, 999999999)}" if random.random() > 0.25 else None,
                source="Demo Sample Data"
            ))

        db.add_all(rows)
        db.commit()
        print(f"Inserted {len(rows)} synthetic demo listings.")
        print("Reminder: these are sample records, not real scraped businesses.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
