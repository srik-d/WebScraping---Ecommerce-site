import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    return soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")

def extract_product_data(box):
    try:
        name = box.find("a", class_="title").text.strip()
        price = box.find("h4", class_="price").text.strip()
        description = box.find("p", class_="description").text.strip()
        rating_div = box.find("div", class_="ratings")
        reviews = rating_div.find("p", class_="review-count").text.strip()
        stars = len(rating_div.find_all("span", class_="ws-icon ws-icon-star"))
        rating = f"{reviews} ({stars} stars)"
        return {"name": name, "price": price, "description": description, "rating": rating}
    except AttributeError as e:
        print(f"Error extracting product data: {e}")
        return None

def scrape_products(url):
    html = fetch_page(url)
    if not html:
        return []

    boxes = parse_html(html)
    products = [extract_product_data(box) for box in boxes if extract_product_data(box)]
    return products

def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Name", "Price", "Description", "Ratings", "Date and Time"])
        for product in data:
            csvwriter.writerow([product["name"], product["price"], product["description"], product["rating"], datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def main():
    print('Scraping e-commerce site...')
    data = scrape_products(url)
    if data:
        filename = f"data_{datetime.now().strftime('%Y-%m-%d')}.csv"
        save_to_csv(data, filename)
        print(f"Data has been successfully scraped and saved to {filename}")
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()
