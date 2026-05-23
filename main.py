import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import os

BASE_URL = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "FernandoCrawlerBot/1.0"
}

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def fetch_page(url):
    response = requests.get(url, headers=HEADERS)
    response.encoding = "utf-8"
    return response.text


def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")

    books = []

    articles = soup.find_all("article", class_="product_pod")

    for article in articles:

        title = article.h3.a["title"]

        price_text = article.find(
            "p",
            class_="price_color"
        ).text

        price = float(
            price_text.replace("£", "").replace("Â", "")
        )

        availability = article.find(
            "p",
            class_="instock availability"
        ).text.strip()

        rating_class = article.find(
            "p",
            class_="star-rating"
        )["class"][1]

        rating = RATING_MAP.get(rating_class, 0)

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })

    return books


def scrape_all_pages():

    all_books = []

    page = 1

    while True:

        if page == 1:
            url = BASE_URL
        else:
            url = f"{BASE_URL}catalogue/page-{page}.html"

        print(f"Scraping page {page}...")

        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            break

        response.encoding = "utf-8"

        books = parse_books(response.text)

        all_books.extend(books)

        page += 1

        time.sleep(1)

    return all_books


def save_json(data):
    with open("output/books.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def save_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("output/books.csv", index=False)


def main():

    os.makedirs("output", exist_ok=True)

    books = scrape_all_pages()

    save_json(books)

    save_csv(books)

    print(f"Total books scraped: {len(books)}")


if __name__ == "__main__":
    main()
