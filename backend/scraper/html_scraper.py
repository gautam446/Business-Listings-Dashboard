import argparse
import csv
import requests
from bs4 import BeautifulSoup


def get_text(element):
    return element.get_text(" ", strip=True) if element else ""


def scrape_page(url, name_selector, category_selector, city_selector,
                address_selector, phone_selector):
    response = requests.get(
        url,
        timeout=20,
        headers={"User-Agent": "BusinessListingsStudentProject/1.0"}
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # This simple version expects each listing to be inside an element
    # with the class "business-card". Change it to match an authorized page.
    cards = soup.select(".business-card")
    results = []

    for card in cards:
        name = get_text(card.select_one(name_selector))
        if not name:
            continue
        results.append({
            "business_name": name,
            "category": get_text(card.select_one(category_selector)) or "Unknown",
            "city": get_text(card.select_one(city_selector)) or "Unknown",
            "address": get_text(card.select_one(address_selector)),
            "phone": get_text(card.select_one(phone_selector)),
            "source": url
        })
    return results


def main():
    parser = argparse.ArgumentParser(description="Scrape an authorized static HTML directory page.")
    parser.add_argument("--url", required=True)
    parser.add_argument("--name-selector", required=True)
    parser.add_argument("--category-selector", default=".business-category")
    parser.add_argument("--city-selector", default=".business-city")
    parser.add_argument("--address-selector", default=".business-address")
    parser.add_argument("--phone-selector", default=".business-phone")
    parser.add_argument("--output", default="listings.csv")
    args = parser.parse_args()

    print("Only use this tool on pages you own or are permitted to scrape.")
    listings = scrape_page(
        args.url, args.name_selector, args.category_selector,
        args.city_selector, args.address_selector, args.phone_selector
    )

    if not listings:
        print("No listing cards found. Check the page permission and CSS selectors.")
        return

    with open(args.output, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=listings[0].keys())
        writer.writeheader()
        writer.writerows(listings)

    print(f"Saved {len(listings)} listings to {args.output}")


if __name__ == "__main__":
    main()
