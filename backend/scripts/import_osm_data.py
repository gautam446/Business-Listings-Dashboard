import time
import requests

from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Listing


# Approximate city bounding boxes:
# south, west, north, east

CITIES = {
    "Ahmedabad": (22.90, 72.40, 23.20, 72.80),
    "Surat": (21.00, 72.70, 21.30, 73.00),
    "Vadodara": (22.20, 73.00, 22.45, 73.30),
    "Rajkot": (22.20, 70.70, 22.45, 70.95),
    "Bhavnagar": (21.65, 72.00, 21.90, 72.30)
}

URL = "https://overpass-api.de/api/interpreter"

HEADERS = {
    "User-Agent": (
        "Business-Listings-Dashboard/1.0 "
        "(educational project; contact: gautam446)"
    )
}

session = requests.Session()
session.headers.update(HEADERS)


def get_businesses(city, bbox):

    south, west, north, east = bbox

    query = f"""
    [out:json][timeout:90];

    (
      node["name"]["shop"]({south},{west},{north},{east});
      way["name"]["shop"]({south},{west},{north},{east});

      node["name"]["amenity"]({south},{west},{north},{east});
      way["name"]["amenity"]({south},{west},{north},{east});

      node["name"]["office"]({south},{west},{north},{east});
      way["name"]["office"]({south},{west},{north},{east});

      node["name"]["tourism"]({south},{west},{north},{east});
      way["name"]["tourism"]({south},{west},{north},{east});

      node["name"]["craft"]({south},{west},{north},{east});
      way["name"]["craft"]({south},{west},{north},{east});
    );

    out center tags;
    """

    for attempt in range(1, 4):

        try:
            print(f"Request attempt {attempt}/3...")

            response = session.post(
                URL,
                data={"data": query},
                timeout=(20, 180)
            )

            if response.status_code in (406, 429, 504, 502, 503):
                print(
                    f"Server returned {response.status_code}. "
                    "Waiting before retry..."
                )

                if response.status_code == 406:
                    print("Check User-Agent or server access.")

                time.sleep(60)
                continue

            response.raise_for_status()

            return response.json().get("elements", [])

        except requests.exceptions.RequestException as error:

            print("Request error:", error)

            if attempt < 3:
                time.sleep(30)

        except ValueError as error:

            print("Invalid JSON response:", error)
            break

    return []


def import_data():

    db: Session = SessionLocal()

    total_inserted = 0

    try:

        for city, bbox in CITIES.items():

            print("\n" + "=" * 45)
            print("Fetching:", city)
            print("=" * 45)

            businesses = get_businesses(city, bbox)

            if not businesses:
                print(f"No data received for {city}.")
                continue

            city_inserted = 0

            for item in businesses:

                tags = item.get("tags", {})

                name = tags.get("name")

                if not name:
                    continue

                category = (
                    tags.get("shop")
                    or tags.get("amenity")
                    or tags.get("office")
                    or tags.get("tourism")
                    or tags.get("craft")
                    or "Other"
                )

                address_parts = [
                    tags.get("addr:housenumber"),
                    tags.get("addr:street"),
                    tags.get("addr:suburb"),
                    tags.get("addr:postcode"),
                    city,
                    "Gujarat"
                ]

                address = ", ".join(
                    part for part in address_parts if part
                )

                phone = (
                    tags.get("phone")
                    or tags.get("contact:phone")
                )

                existing = db.query(Listing).filter(
                    Listing.business_name == name,
                    Listing.city == city
                ).first()

                if existing:
                    continue

                listing = Listing(
                    business_name=name,
                    category=category,
                    city=city,
                    address=address,
                    phone=phone,
                    source="OpenStreetMap"
                )

                db.add(listing)

                city_inserted += 1
                total_inserted += 1

            db.commit()

            print("Records received:", len(businesses))
            print("New records inserted:", city_inserted)

            # Avoid sending requests too quickly.
            time.sleep(30)

        print("\n" + "=" * 45)
        print("IMPORT COMPLETED")
        print("Total new records:", total_inserted)
        print("=" * 45)

    except Exception as error:

        db.rollback()

        print("\nDatabase error:", error)

    finally:

        db.close()


if __name__ == "__main__":
    import_data()